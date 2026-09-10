# create_graph.py
# ----------------
# Creates a graph for the Pixela user.
# Requires TOKEN, PIXELA_USERNAME, GRAPH_ID, GRAPH_NAME in .env.
#
# Key lesson (Day 37): the token goes in the *headers*, not the body.
# curl -X POST https://pixe.la/v1/users/a-know/graphs \
#      -H 'X-USER-TOKEN:thisissecret' \
#      -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")
GRAPH_NAME = os.getenv("GRAPH_NAME")


def create_graph():
    """
    Create a graph under the authenticated user.
    Returns True on success, False on failure.
    """
    if not all([TOKEN, PIXELA_USERNAME, GRAPH_ID, GRAPH_NAME]):
        print("Missing one of TOKEN / PIXELA_USERNAME / GRAPH_ID / GRAPH_NAME in .env")
        return False

    graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"

    # Body params
    params = {
        "id": GRAPH_ID,
        "name": GRAPH_NAME,
        "unit": "commit",
        "type": "int",
        "color": "ajisai",
        "description": "My Daily Habit Tracker!",
    }

    # Auth goes in the headers — this is the whole point of Day 37
    headers = {"X-USER-TOKEN": TOKEN}

    try:
        response = requests.post(url=graph_endpoint, json=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        print(data)
        if data.get("isSuccess"):
            # This URL opens the graph in a browser
            print(f"Graph URL: {graph_endpoint}/{GRAPH_ID}.html")
        return data.get("isSuccess", False)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False


if __name__ == "__main__":
    create_graph()