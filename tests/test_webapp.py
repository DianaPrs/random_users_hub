from unittest.mock import Mock, patch

import pytest

from webapp import create_app


@pytest.fixture(scope='module')
def test_client():
    """"Create a test client"""
    app = create_app('flask_test.cfg')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client 


def test_main_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_user_profile(test_client):
    with patch("pymongo.collection.Collection.find") as FindMmock:
      FindMock = Mock()
      FindMock.return_value = Mock()
      response = test_client.get('/')
      assert response.status_code == 200


def test_new_user_get(test_client):
    response = test_client.get('/user/new')
    assert response.status_code == 200

