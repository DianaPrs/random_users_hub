from unittest.mock import Mock, patch

from webapp import create_app
from webapp.upload_user import get_user


def test_get_user():
    app = create_app("flask_test.cfg")
    with app.app_context():
        with patch("requests.get") as MockTask:
            MockTask.return_value.raise_for_status = Mock()
            MockTask.return_value.json.return_value = {
                "results": [
                    {
                        "gender": "male",
                        "name": {"first": "Mikkel", "last": "Alstad"},
                        "location": {
                            "street": {"number": 8393, "name": "Brettevilles gate"},
                            "city": "Vågsvåg",
                            "country": "Norway",
                        },
                        "email": "mikkel.alstad",
                        "cell": "46133606",
                        "picture": {
                            "large": "https://randomuser.me/api/portraits/men/76.jpg"
                        },
                    }
                ]
            }
            assert get_user(1) == False


def test_get_user_not_valid_data():
    app = create_app("flask_test.cfg")
    with app.app_context():
        with patch("requests.get") as MockTask:
            MockTask.return_value.raise_for_status = Mock()
            MockTask.return_value.json.return_value = {
                "results": {"name": {"first": "foo", "last": "bar"}}
            }
            assert get_user(1) == False
