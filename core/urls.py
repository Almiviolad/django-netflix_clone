from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('movie/<str:pk>/', views.movie_details, name='movie_details'),
    path('logout', views.logout, name='logout'),
    ]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)