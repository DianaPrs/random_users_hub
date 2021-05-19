from unittest.mock import Mock, patch

import pytest
from flask import url_for
from webapp import create_app
from webapp.forms import UserForm
from bson.objectid import ObjectId


@pytest.fixture(scope="module")
def test_client():
    """ "Create a test client"""
    app = create_app("flask_test.cfg")
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


def test_main_page(test_client):
    """Test main page"""
    with patch("pymongo.collection.Collection.find"):
        FindMock = Mock()
        FindMock.return_value = Mock()
        response = test_client.get("/")
        assert response.status_code == 200


def test_user_profile(test_client):
    """Test user profile page"""
    response = test_client.get("/")
    assert response.status_code == 200


def test_upload(test_client):
    """Test upload user route"""
    response = test_client.post("/upload", data=dict(number=1), follow_redirects=True)
    with patch("webapp.upload_user.get_user") as MockFunc:
        MockFunc.return_value = {}
        assert response.status_code == 200


def test_new_user_get(test_client):
    """Test new user page get"""
    response = test_client.get("/user/new")
    assert response.status_code == 200


def test_new_user_post(test_client):
    """Test new user page post"""
    form = UserForm()
    response = test_client.post("/user/new", data=form.data)
    assert response.status_code == 200


def test_update_user_get(test_client):
    """Test update user"""
    with patch("flask_pymongo.wrappers.Collection.find_one_or_404"):
        user_id = ObjectId()
        url = url_for("update_user", user_id=user_id)
        response = test_client.get(url)
        assert response.status_code == 200


def test_random_user(test_client):
    """Test random user endpoint"""
    response = test_client.get("/random")
    assert response.status_code == 200


def test_delete_user(test_client):
    """Test dalete user endpoint"""
    user_id = ObjectId()
    url = url_for("delete_user", user_id=user_id)
    response = test_client.get(url, follow_redirects=True)
    assert response.status_code == 200
