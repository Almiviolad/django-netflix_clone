import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from core.models import Movie, Genre


API_KEY = 'c42c1fcf17d8bff1d212ed96c1cac58f'
BASE_URL = "https://api.themoviedb.org/3"

# gets the movie genres from TMDB
def fetch_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        for genre in genres:
            Genre.objects.update_or_create(
                tmdb_id = genre["id"],
                genre_name = genre['name']
            )
    else:
        print('cannot fetch genres')

# get the img for the movie
def get_pics(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.content
    else:
        raise Exception('Failed to download Image')

# populates the DB with movies details from TMDB
class Command(BaseCommand):
    help = 'Populates the database with popular movies from TMDb'

    def handle(self, *args, **kwargs):
        url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=en-US&page=1"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch movies from TMDb")
            return
        
        fetch_genres()
        movies = response.json().get("results", [])
        for movie_data in movies:
            title = movie_data["title"]
            poster_path = movie_data["poster_path"]
            full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"


            # Save to DB
            if title and poster_path:
                if not Movie.objects.filter(title=title).exists():
                    movie = Movie.objects.create(
                        title=title,
                        release_date=movie_data["release_date"],
                        overview=movie_data["overview"],
                        popularity=movie_data["popularity"]
                    )
                    file_name = full_poster_url.split('/')[-1]
                    try:
                        img = get_pics(full_poster_url)
                        movie.poster.save(file_name, ContentFile(img), save=True)
                    except Exception as e:
                        self.stderr.write(e)
                    genre_ids = movie_data.get("genre_ids", [])
                    genres = Genre.objects.filter(tmdb_id__in=genre_ids)
                    movie.genres.set(genres)
                    self.stdout.write(f"Saved {title} movie")
                else:
                    self.stderr.write('movie already exists')