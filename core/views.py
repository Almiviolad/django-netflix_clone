from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Genre

# Create your views here.
def index(request):
    user = request.user
    return render(request, 'index.html', {'user': user} )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #autheticates user (checks if passwordandusername is corect)
        auth_user = authenticate(request, username=username, password=password)
        if auth_user:
            user_login(request, auth_user)
            return redirect('/recommendations')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                messages.color = 'red'
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                messages.color = 'red'
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'Signed up successfully')
                messages.color = 'green'
                user_login(request, user)
                return redirect('/recommendations')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:   
        return render(request, 'signup.html')
    

@login_required
def recommendations(request):
    movies = Movie.objects.all()
    return render(request, "recommendations.html", {'movies': movies})


def movie_details(request, pk):
    movie = Movie.objects.get(movie_id=pk)
    return render(request, 'movie_details.html', {'movie': movie})

@login_required
def logout(request):
    user_logout(request)
    return redirect('login')