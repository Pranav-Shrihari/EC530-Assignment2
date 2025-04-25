import pytest
from fastapi.testclient import TestClient
from APIs import app  # Assuming your FastAPI app is in APIs.py

# Test data
user_info = {'id': 1, 'name': 'Pranav Shrihari', 'email': 'pranavsh@bu.edu', 'phone': '123-456-7890'}
house_info = {'id': 1, 'name': 'Myles', 'address': '610 Beacon St'}
room_info = {'id': 1, 'name': 'My Dorm', 'floor': 9, 'size': '200 sq ft'}  # floor should be int, not str
device_info = {'id': 1, 'name': 'Smart Light'}

@pytest.fixture
def client():
    """Set up a FastAPI TestClient"""
    return TestClient(app)

# ---------------- User Tests ----------------
def test_create_user(client):
    response = client.post('/users', json=user_info)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Pranav Shrihari'

def test_get_user(client):
    client.post('/users', json=user_info)
    response = client.get('/users/1')
    assert response.status_code == 200
    data = response.json()
    assert data['email'] == 'pranavsh@bu.edu'

def test_update_user(client):
    client.post('/users', json=user_info)
    updated_user_info = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'phone': '987-654-3210'}
    response = client.put('/users/1', json=updated_user_info)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'John Doe'

def test_delete_user(client):
    client.post('/users', json=user_info)
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'User deleted'

# ---------------- House Tests ----------------
def test_create_house(client):
    client.post('/users', json=user_info)
    response = client.post('/users/1/houses', json=house_info)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Myles'

def test_get_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.get('/users/1/houses/1')
    assert response.status_code == 200
    data = response.json()
    assert data['address'] == '610 Beacon St'

def test_update_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    updated_house_info = {'id': 1, 'name': 'New Myles', 'address': '123 New St'}
    response = client.put('/users/1/houses/1', json=updated_house_info)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'New Myles'

def test_delete_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.delete('/users/1/houses/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'House deleted'

# ---------------- Room Tests ----------------
def test_create_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.post('/users/1/houses/1/rooms', json=room_info)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'My Dorm'

def test_get_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.get('/users/1/houses/1/rooms/1')
    assert response.status_code == 200
    data = response.json()
    assert data['floor'] == 9

def test_update_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    updated_room_info = {'id': 1, 'name': 'New Dorm', 'floor': 10, 'size': '300 sq ft'}
    response = client.put('/users/1/houses/1/rooms/1', json=updated_room_info)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'New Dorm'

def test_delete_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.delete('/users/1/houses/1/rooms/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'Room deleted'

# ---------------- Device Tests ----------------
def test_create_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Smart Light'

def test_get_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    response = client.get('/users/1/houses/1/rooms/1/devices/1')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Smart Light'

def test_update_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    updated_device_info = {'id': 1, 'name': 'Smart Thermostat'}
    response = client.put('/users/1/houses/1/rooms/1/devices/1', json=updated_device_info)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Smart Thermostat'

def test_delete_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    response = client.delete('/users/1/houses/1/rooms/1/devices/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'Device deleted'

# Main trigger (optional)
if __name__ == '__main__':
    pytest.main()
