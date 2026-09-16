# empire_movies.py
# -----------------
# Scrapes Empire Online's "100 Greatest Movies" list.
#
# Key insight: the page is a Next.js app. The movie data lives in a
# JSON blob inside <script id="__NEXT_DATA__">, not in rendered HTML.
# We parse that JSON instead of hunting for h2/img/p tags.

import json
import re
import sys

import requests
from bs4 import BeautifulSoup

SITE_URL = "https://www.empireonline.com/movies/features/best-movies-2/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 15
FILE_URL = "./data.json"

# Fallback regex if __NEXT_DATA__ is ever missing
MOVIE_RE = re.compile(r"^\s*(\d+)\)\s*(.+?)\s*\((\d{4})\)\s*$")


def fetch_soup(url):
    """Fetch the page and return a BeautifulSoup object, or None on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def extract_next_data(soup):
    """
    Pull the __NEXT_DATA__ JSON blob out of the page.
    Returns a dict, or None if the script tag is missing/unparseable.
    """
    script = soup.select_one("script#__NEXT_DATA__")
    if script is None:
        print("Warning: __NEXT_DATA__ not found. Page structure may have changed.")
        return None

    try:
        return json.loads(script.string)
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Warning: could not parse __NEXT_DATA__ JSON: {e}")
        return None


def find_movie_entries(node):
    """
    Recursively walk the JSON tree and yield every dict that looks like
    a movie entry (has 'title' and 'meta' or 'rank' keys).

    Next.js apps nest data unpredictably, so a recursive search is more
    robust than hard-coding a path like data['props']['pageProps']['...'].
    """
    if isinstance(node, dict):
        # Heuristic: a movie entry typically has a title and either
        # a numeric rank or a "meta" string containing the year.
        if "title" in node and ("rank" in node or "meta" in node):
            yield node
        for value in node.values():
            yield from find_movie_entries(value)

    elif isinstance(node, list):
        for item in node:
            yield from find_movie_entries(item)


def parse_movie(entry):
    """
    Convert a raw JSON entry into our flat dict format.
    Returns None if the entry lacks required fields.
    """
    title = entry.get("title")
    if not title:
        return None

    rank = entry.get("rank")
    meta = entry.get("meta", "")   # e.g. "(1994)"

    # Extract year from meta string like "(1994)"
    year = None
    year_match = re.search(r"\((\d{4})\)", str(meta))
    if year_match:
        year = int(year_match.group(1))

    # Image URL — key name varies ("image", "imageUrl", "src")
    img_url = None
    for key in ("imageUrl", "image", "src"):
        if entry.get(key):
            img_url = entry[key]
            break

    return {
        "rank": int(rank) if rank is not None else None,
        "title": title.strip(),
        "year": year,
        "img_url": img_url,
        "director": entry.get("director"),
        "starring": entry.get("starring"),
    }


def scrape_movies(soup):
    """
    Scrape the movie list.
    Strategy 1: parse the embedded __NEXT_DATA__ JSON.
    Strategy 2 (fallback): parse visible HTML with the regex.

    Returns a list of movie dicts sorted by rank ascending (1 → 100).
    """
    next_data = extract_next_data(soup)

    if next_data:
        raw_entries = list(find_movie_entries(next_data))
        movies = [parse_movie(e) for e in raw_entries]
        # Drop None results and entries without a rank
        movies = [m for m in movies if m and m["rank"] is not None]

        if movies:
            movies.sort(key=lambda m: m["rank"])
            return movies

        print("No movies found in __NEXT_DATA__. Trying HTML fallback...")

    # ---- Fallback: parse visible HTML ----
    return scrape_movies_from_html(soup)


def scrape_movies_from_html(soup):
    """Fallback parser: walk h2 / img / p tags in document order."""
    movies = []
    current = None

    for tag in soup.find_all(["h2", "img", "p"]):
        if tag.name == "h2":
            match = MOVIE_RE.match(tag.get_text(strip=True))
            if match:
                if current:
                    movies.append(current)
                current = {
                    "rank": int(match.group(1)),
                    "title": match.group(2).strip(),
                    "year": int(match.group(3)),
                    "img_url": None,
                    "director": None,
                    "starring": None,
                }
            continue

        if current is None:
            continue

        if tag.name == "img" and current["img_url"] is None:
            current["img_url"] = tag.get("src")
            continue

        if tag.name == "p" and current["director"] is None:
            txt = tag.get_text(" ", strip=True)
            if "Director:" in txt and "Starring:" in txt:
                dir_part, star_part = txt.split("Starring:", 1)
                current["director"] = dir_part.split("Director:", 1)[1].strip()
                current["starring"] = star_part.strip()

    if current:
        movies.append(current)

    movies.sort(key=lambda m: m["rank"])
    return movies


def write_file(movies_data):
    """Write the scraped movies to a JSON file. Returns True on success."""
    if not movies_data:
        print("Refusing to write empty data. Scrape may have failed.")
        return False

    try:
        with open(FILE_URL, "w", encoding="utf-8") as f:
            json.dump({"data": movies_data}, f, indent=4, ensure_ascii=False)
        print(f"Wrote {len(movies_data)} movies to {FILE_URL}")
        return True
    except OSError as e:
        print(f"Could not write {FILE_URL}: {e}")
        return False
    except TypeError as e:
        print(f"Data is not JSON-serialisable: {e}")
        return False


def main():
    soup = fetch_soup(SITE_URL)
    if soup is None:
        print("Could not load the page. Exiting.")
        sys.exit(1)

    movies = scrape_movies(soup)

    if not movies:
        print("No movies scraped. The site structure may have changed.")
        sys.exit(1)

    write_file(movies)


if __name__ == "__main__":
    main()