# post_a_pixel.py
# ----------------
# Posts (or increments) a pixel for today's date.
# Requires TOKEN, PIXELA_USERNAME, GRAPH_ID in .env.
#
# Logic:
# - GET the pixel for today.
#   - 200  → pixel exists, read its quantity.
#   - 404  → pixel doesn't exist, treat as 0.
# - POST the new quantity (old + 1).

import os
import requests
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

TOKEN = os.getenv("TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# Today's date in Pixela's expected format: YYYYMMDD
NOW = dt.now().strftime("%Y%m%d")

HEADERS = {"X-USER-TOKEN": TOKEN}


def check_for_pixel(date):
    """
    Return the pixel quantity for the given date.
      200 → real quantity (int)
      404 → 0 (pixel not created yet)
    Any other status raises HTTPError.
    """
    pixel_endpoint = (
        f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date}"
    )
    response = requests.get(url=pixel_endpoint, headers=HEADERS)

    if response.status_code == 200:
        return int(response.json()["quantity"])
    if response.status_code == 404:
        return 0

    # Any other status (3xx, 4xx, 5xx) → raise so the caller can handle it
    response.raise_for_status()
    # If somehow we get here (e.g. a 3xx that requests doesn't follow),
    # raise explicitly rather than silently returning None.
    raise requests.exceptions.RequestException(
        f"Unexpected status {response.status_code} when checking pixel."
    )


def post_a_pixel():
    """
    If a pixel exists for today, increment it; otherwise create it with quantity 1.
    Returns True on success, False on failure.
    """
    if not all([TOKEN, PIXELA_USERNAME, GRAPH_ID]):
        print("Missing one of TOKEN / PIXELA_USERNAME / GRAPH_ID in .env")
        return False

    graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
    pixel_endpoint = f"{graph_endpoint}/{NOW}"

    try:
        # Both the GET (check) and POST (write) live inside the try so any
        # network problem is handled the same way.
        pixel = check_for_pixel(NOW)
        quantity = str(pixel + 1)

        params = {"date": NOW, "quantity": quantity}

        response = requests.post(url=graph_endpoint, json=params, headers=HEADERS)
        response.raise_for_status()

        print(response.text)
        print(f"{NOW}: ADDED => {pixel_endpoint}")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"HTTP {e.response.status_code}: {e.response.text}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Network issue: {e}")
        return False


if __name__ == "__main__":
    post_a_pixel()
