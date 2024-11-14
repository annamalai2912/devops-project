import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json()['status'] == 'healthy'

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert 'message' in rv.get_json()