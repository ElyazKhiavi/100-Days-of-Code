# create_account.py
# ------------------
# Creates a Pixela user account.
# Requires TOKEN and PIXELA_USERNAME in .env.

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def create_account():
    """
    Create a Pixela user account.
    Note: the token and username go in the JSON body — this is an unauthenticated
    request (there's no user yet to authenticate as).
    Returns True on success, False on failure.
    """
    # Guard against missing env vars
    if not TOKEN or not PIXELA_USERNAME:
        print("Missing TOKEN or PIXELA_USERNAME in .env")
        return False

    # Body params (Pixela expects these as JSON, not headers)
    params = {
        "token": TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    try:
        response = requests.post(url=PIXELA_ENDPOINT, json=params)
        response.raise_for_status()

        # Pixela returns {"message": "...", "isSuccess": true/false}
        data = response.json()
        print(data)
        return data.get("isSuccess", False)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False


if __name__ == "__main__":
    create_account()

