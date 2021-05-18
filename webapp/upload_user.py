from typing import Dict, List, Optional

import requests
from flask import current_app
from jsonschema import ValidationError, validate

from .json_schema import schema


def get_user(number_of_users: int) -> Optional[List[Dict[str, Dict]]]:
    """Send request to external API

    :param number_of_users: the number of users entries that will be loaded
    :return list of dictionaries containing user data, where
    keys: name, gender, cell, email, location, picture
    """
    randomuser_url = current_app.config["RANDOMUSER_URL"]
    params = {
        "results": number_of_users,
        "inc": "name,gender,cell,email,location,picture",
    }
    try:
        result = requests.get(randomuser_url, params=params)
        result.raise_for_status()
        data = result.json()
        results = data.get("results")
        if results:
            try:
                validate_data(data)
                return results
            except (IndexError, TypeError):
                return False
    except (requests.RequestException, ValueError):
        print("Network error")
        return False


def validate_data(content: Dict[str, Dict], schema=schema) -> None:
    """Validate JSON data

    :param content: Json data
    :param schema: json schema
    """
    try:
        validate(content, schema)
    except ValidationError as ex:
        raise Exception(ex.message)
