# Nested Lists and Dictionaries


# You can nest lists in dicts, nested lists in dicts, dicts in dicts and much more in python
# there truly is not limit to what you can do so you should be abel to pull of what you desire with them


movies = {
    "Fight Club": {
        "year": 1999,
        "actors/characters": {
            "Edward Norton": "The Narrator",
            "Brad Pitt": "Tyler Durden",
            "Helena Bonham Carter": "Marla Singer",
            "Jared Leto": "Angel Face",
        },
        "director": "David Fincher",
        "genre": [
            "Action",
            "Comedy",
            "Thriller",
            "Dark comedy",
            "Drama",
            "Suspense",
            "Crime film",
            "Mystery",
            "crime fiction",
        ],
    },
    "Pulp Fiction": {
        "year": 1994,
        "actors/characters": {
            "John Travolta": "Vincent Vega",
            "Samuel L. Jackson": "Jules Winnfield",
            "Uma Thurman": "Mia Wallace",
            "Bruce Willis": "Butch Coolidge",
        },
        "director": "Quentin Tarantino",
        "genre": [
            "Crime",
            "Drama",
            "Thriller",
            "Black comedy",
            "Neo-noir",
        ],
    },
    "The Dark Knight": {
        "year": 2008,
        "actors/characters": {
            "Christian Bale": "Bruce Wayne / Batman",
            "Heath Ledger": "Joker",
            "Aaron Eckhart": "Harvey Dent",
            "Michael Caine": "Alfred Pennyworth",
        },
        "director": "Christopher Nolan",
        "genre": [
            "Action",
            "Crime",
            "Drama",
            "Thriller",
            "Superhero",
        ],
    },
}




print(movies["Fight Club"]["actors/characters"]["Edward Norton"]) # The Narrator
print(movies["The Dark Knight"]["genre"]) # ['Action', 'Crime', 'Drama', 'Thriller', 'Superhero']
print(movies["Pulp Fiction"]["year"]) # 1994
