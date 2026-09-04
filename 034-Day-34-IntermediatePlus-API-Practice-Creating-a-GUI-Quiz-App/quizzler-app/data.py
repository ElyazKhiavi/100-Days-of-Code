import requests

API_URL = "https://opentdb.com/api.php?amount=10&category=15&type=boolean"  # this includes the parameters we don't need to include them


# ----with params used----

RAW_API_URL = "https://opentdb.com/api.php"

# 'https://opentdb.com/api.php?amount=10&category=15&type=boolean'
# ?amount=10
params = {"amount": 10, "category": 15, "type": "boolean"}


def get_questions():
    connection = requests.get(RAW_API_URL, params=params)
    # connection.raise_for_status()
    data = connection.json()["results"]
    return data


for i, q in enumerate(get_questions(), 1):
    print(i, q["question"], q["correct_answer"])
