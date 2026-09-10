# delete_pixel.py
# ----------------
# Deletes a pixel (a day's record) from the graph.
# Requires TOKEN, PIXELA_USERNAME, GRAPH_ID in .env.
#
# Note: the date is hardcoded below. In a real program you'd pass it as an
# argument or ask the user. For this practice exercise we set it manually.

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

DATE = "20260910"   # YYYYMMDD


def delete_pixel(date=DATE):
    """
    Delete the pixel for the given date.
    Returns True on success, False on failure.
    """
    if not all([TOKEN, PIXELA_USERNAME, GRAPH_ID]):
        print("Missing one of TOKEN / PIXELA_USERNAME / GRAPH_ID in .env")
        return False

    pixel_endpoint = (
        f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date}"
    )
    headers = {"X-USER-TOKEN": TOKEN}

    # curl -X DELETE https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 \
    #      -H 'X-USER-TOKEN:thisissecret'
    try:
        response = requests.delete(url=pixel_endpoint, headers=headers)
        response.raise_for_status()
        print(response.text)
        return True

    except requests.exceptions.HTTPError as e:
        # 404 here means there was no pixel for that date
        print(f"HTTP {e.response.status_code}: {e.response.text}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Network issue: {e}")
        return False


if __name__ == "__main__":
    delete_pixel()