from unittest.mock import Mock, patch

from webapp import create_app
from webapp.upload_user import get_user


def test_get_user():
    """Test get_user fanction with valid data"""
    app = create_app("flask_test.cfg")
    with app.app_context():
        with patch("requests.get") as MockTask:
            MockTask.return_value.raise_for_status = Mock()
            MockTask.return_value.json.return_value = {
                "results": [
                    {
                        "gender": "male",
                        "name": {"title": "Mr", "first": "Felix", "last": "Hansen"},
                        "location": {
                            "street": {"number": 5177, "name": "Hyldevej"},
                            "city": "Gørløse",
                            "country": "Denmark",
                        },
                        "email": "felix.hansen@example.com",
                        "cell": "29130618",
                        "picture": {
                            "large": "https://randomuser.me/api/portraits/men/76.jpg",
                            "medium": "https://randomuser.me/api/portraits/med/men/76.jpg",
                            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/76.jpg",
                        },
                    }
                ]
            }
            assert isinstance(get_user(1), list)


def test_get_user_not_valid_data():
     """Test get_user fanction with not valid data"""
    app = create_app("flask_test.cfg")
    with app.app_context():
        with patch("requests.get") as MockTask:
            MockTask.return_value.raise_for_status = Mock()
            MockTask.return_value.json.return_value = {
                "results": {"name": {"first": "foo", "last": "bar"}}
            }
            assert get_user(1) == False
