import requests

RAW_API_URL = "https://opentdb.com/api.php"
PARAMS = {"amount": 10, "category": 15, "type": "boolean"}


def get_questions():
    response = requests.get(RAW_API_URL, params=PARAMS)
    response.raise_for_status()
    data = response.json()["results"]
    return data


question_data = get_questions()
