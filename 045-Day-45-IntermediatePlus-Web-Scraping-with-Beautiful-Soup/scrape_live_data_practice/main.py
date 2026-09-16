from bs4 import BeautifulSoup
import requests

SITE_URL = "https://news.ycombinator.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (HN top-post scraper)"}
TIMEOUT = 10   # seconds


def fetch_soup(url):
    """Fetch the page and return a BeautifulSoup object, or None on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
        return None


def find_top_post(soup):
    """
    Walk the front page and return the post with the highest score.
    Returns None if no scored posts are found.
    """
    highest = None   # we haven't seen a scored post yet

    for row in soup.select("tr.athing"):
        # --- Title row ---
        title_tag = row.select_one(".titleline > a")
        if title_tag is None:
            continue   # malformed row; skip rather than crash
        title = title_tag.get_text(strip=True)
        link = title_tag["href"]

        # --- Subtext row (sits directly after the title row) ---
        subtext_row = row.find_next_sibling("tr")
        score_tag = subtext_row.select_one(".score") if subtext_row else None
        score = int(score_tag.get_text(strip=True).split()[0]) if score_tag else None

        # Update the running maximum only for posts that have a score
        if score is not None and (highest is None or score > highest["score"]):
            highest = {"title": title, "link": link, "score": score}

        # --- Print this row ---
        score_display = f"{score} Upvotes:" if score is not None else "no score"
        print(f"{score_display:>12}  {title}")
        print(f"            {link}")
        print()

    return highest


def main():
    soup = fetch_soup(SITE_URL)
    if soup is None:
        print("Could not load the site. Exiting.")
        return   # stop here — nothing else to do

    highest = find_top_post(soup)

    print("-------------------Highest Upvotes-------------------")
    if highest is None:
        print("No scored posts found.")
    else:
        print(f"{highest['score']:>10}  {highest['title']}")
        print(f"            {highest['link']}")


if __name__ == "__main__":
    main()