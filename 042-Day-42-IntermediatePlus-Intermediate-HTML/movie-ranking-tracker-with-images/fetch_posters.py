import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Set your TMDB API key here
API_KEY = os.getenv('API_KEY')

# Movie list with exact titles and IMDb IDs from your table
MOVIES = [
    ("Sicario: Day of the Soldado (2018)", "tt5052474"),
    ("Tuner (2025)", "tt33296751"),
    ("I Swear (2025)", "tt31514146"),
    ("Finding Emily (2026)", "tt32499466"),
    ("Masters of the Universe (2026)", "tt0427340"),
    ("Soulm8te (2026)", "tt32654916"),
    ("The Sheep Detectives (2026)", "tt32565993"),
    ("Scary Movie (2026)", "tt32093575"),
    ("Supergirl (2026)", "tt8814476"),
    ("Insomnia (2002)", "tt0278504"),
    ("Pressure (2026)", "tt32547691"),
    ("Speak No Evil (2022)", "tt14253846"),
    ("Good Luck, Have Fun, Don't Die (2025)", "tt1341338"),
    ("The Usual Suspects (1995)", "tt0114814"),
    ("Split (2016)", "tt4972582"),
    ("The Legend of Hei 2 (2025)", "tt37284198"),
    ("Minions & Monsters (2026)", "tt32890033"),
    ("Mutiny (2026)", "tt32338669"),
]

def fetch_poster_urls():
    base_image_url = "https://image.tmdb.org/t/p/w1280"
    
    print(f"{'Movie Title':<45} | {'TMDB Poster Link'}")
    print("-" * 115)
    
    for title, imdb_id in MOVIES:
        api_url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={API_KEY}&external_source=imdb_id"
        
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            
            # Check movie_results, tv_results, etc.
            movie_results = data.get("movie_results", [])
            
            if movie_results and movie_results[0].get("poster_path"):
                poster_path = movie_results[0]["poster_path"]
                full_poster_url = f"{base_image_url}{poster_path}"
                print(f"{title:<45} | {full_poster_url}")
            else:
                print(f"{title:<45} | Poster path not found on TMDB")
                
        except requests.exceptions.RequestException as e:
            print(f"{title:<45} | Error fetching data: {e}")

if __name__ == "__main__":
    fetch_poster_urls()