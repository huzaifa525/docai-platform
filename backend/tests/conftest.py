import pytest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True
    DEEPSEEK_API_KEY = 'test-key'

@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers():
    return {'Authorization': 'Bearer test-token'}