from flask import current_app
import requests


def get_user(number_of_users: int):
    """"""
    randomuser_url = current_app.config["RANDOMUSER_URL"]
    params = {
        "results": number_of_users,
        "inc": "name,gender,cell,email,location,picture",
    }
    try:
        result = requests.get(randomuser_url, params=params)
        result.raise_for_status()
        data = result.json()
        if "results" in data:
            try:
                return data["results"]
            except(IndexError, TypeError):
                return False
    except(requests.RequestException, ValueError):
        print('Network error')
        return False
