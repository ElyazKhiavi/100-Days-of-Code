# workout-tracker/main.py
# ------------------------
# Asks the user what exercise they did, sends it to the Nutritionix API to get
# duration and calories, then appends the result as a new row in a Google Sheet
# via Sheety.
#
# Requires in .env:
#   NUTRITION_API_APP_ID, NUTRITION_API_KEY
#   SHEETY_API_TOKEN, SHEETY_ENDPOINT

import os
import requests
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------
# Nutritionix (exercise lookup) configuration
# ------------------------------------------------------------------
NUTRITION_API_APP_ID = os.getenv("NUTRITION_API_APP_ID")
NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
NUTRITION_API_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
NUTRITION_API_HEADERS = {
    "x-app-id": NUTRITION_API_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json",
}

# Hardcoded personal data (change to match your own info)
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 20
GENDER = "male"

# ------------------------------------------------------------------
# Sheety (Google Sheets) configuration
# ------------------------------------------------------------------
SHEETY_API_TOKEN = os.getenv("SHEETY_API_TOKEN")
SHEETY_ENDPOINT = os.getenv(
    "SHEETY_ENDPOINT"
)  # full URL, e.g. https://api.sheety.co/user/project/sheet
SHEETY_API_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_API_TOKEN,
}


def get_user_activity():
    """Prompt the user for what they did. Keep asking until non-empty. Return the string."""
    while True:
        activity = input("Tell me which exercises you did: ").strip()
        if not activity:
            print("You must not leave this blank!")
            continue
        # API caps the query at 50 characters
        if len(activity) > 50:
            print("Please keep it under 50 characters.")
            continue
        return activity


def nutrition_api_call():
    """
    Ask the user for an exercise, send it to Nutritionix, and return
    (duration_min, calories, exercise_name) as strings.
    Returns (None, None, None) on failure.
    """
    # Validate BOTH credentials are present (all() not any())
    if not all([NUTRITION_API_APP_ID, NUTRITION_API_KEY]):
        print("Missing Nutritionix credentials in .env")
        return None, None, None

    activity = get_user_activity()
    print("Looking up your activity...")

    # Build params locally instead of mutating a module-level dict
    params = {
        "query": activity,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
        "gender": GENDER,
    }

    try:
        response = requests.post(
            url=NUTRITION_API_ENDPOINT,
            json=params,
            headers=NUTRITION_API_HEADERS,
        )
        response.raise_for_status()

        # if the API ever returns zero matches for a weird query
        exercises = response.json().get("exercises", [])
        if not exercises:
            print("No match found for that activity.")
            return None, None, None
        result = exercises[0]

        return (
            str(result["duration_min"]),
            str(result["nf_calories"]),
            result["name"].title(),
        )

    except requests.exceptions.RequestException as e:
        print(f"Something went wrong talking to Nutritionix: {e}")
        return None, None, None


def send_data_to_sheety(params):
    """
    POST a new row to the Sheety sheet.
    Returns True on success, False on failure.
    """
    # Same fix here: ALL credentials must be present
    if not all([SHEETY_API_TOKEN, SHEETY_ENDPOINT]):
        print("Missing Sheety credentials in .env")
        return False

    try:
        response = requests.post(
            url=SHEETY_ENDPOINT,
            headers=SHEETY_API_HEADERS,
            json=params,
        )
        # raise_for_status() already guarantees success if we reach the next line
        response.raise_for_status()
        return True

    except requests.exceptions.RequestException as e:
        print(f"Something went wrong talking to Sheety: {e}")
        return False


def main():
    date_str = dt.now().strftime("%Y-%m-%d")
    time_str = dt.now().strftime("%H:%M:%S")

    duration, calories, exercise_name = nutrition_api_call()

    # Any of the three being None/empty means the lookup failed
    if not all([duration, calories, exercise_name]):
        print("Could not retrieve exercise data. Aborting.")
        return

    # Sheety expects the payload wrapped under the sheet name ("workout")
    sheety_params = {
        "workout": {
            "date": date_str,
            "time": time_str,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }

    if send_data_to_sheety(sheety_params):
        print("Data added successfully.")
    else:
        print("There was a problem while adding the data.")


if __name__ == "__main__":
    main()
