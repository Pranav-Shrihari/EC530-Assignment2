import pytest
from APIs import app

user_info = {'id': 1, 'name': 'Pranav Shrihari', 'email': 'pranavsh@bu.edu', 'phone': '123-456-7890'}
house_info = {'id': 1, 'name': 'Myles', 'address': '610 Beacon St'}
room_info = {'id': 1, 'name': 'My Dorm', 'floor': '9', 'size': '200 sq ft'}
device_info = {'id': 1, 'name': 'Smart Light'}

@pytest.fixture
def client():
    """Set up a test client for testing"""
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/users', json=user_info)
    assert response.status_code == 201
    response_data = response.get_data(as_text=True)
    assert 'User created:' in response_data
    assert 'Pranav Shrihari' in response_data

def test_get_user(client):
    client.post('/users', json=user_info)
    response = client.get('/users/1')
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'User found:' in response_data
    assert 'Pranav Shrihari' in response_data

def test_update_user(client):
    client.post('/users', json=user_info)
    updated_user_info = {'name': 'John Doe', 'email': 'john@example.com', 'phone': '987-654-3210'}
    response = client.put('/users/1', json=updated_user_info)
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'User updated:' in response_data
    assert 'John Doe' in response_data

def test_delete_user(client):
    client.post('/users', json=user_info)
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert 'User deleted successfully' in response.get_data(as_text=True)

def test_create_house(client):
    client.post('/users', json=user_info)
    response = client.post('/users/1/houses', json=house_info)
    assert response.status_code == 201
    response_data = response.get_data(as_text=True)
    assert 'House created:' in response_data
    assert 'Myles' in response_data
    assert '610 Beacon St' in response_data

def test_get_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.get('/users/1/houses/1')
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'House found:' in response_data
    assert 'Myles' in response_data
    assert '610 Beacon St' in response_data

def test_update_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    updated_house_info = {'name': 'New Myles', 'address': '123 New St'}
    response = client.put('/users/1/houses/1', json=updated_house_info)
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'House updated:' in response_data
    assert 'New Myles' in response_data

def test_delete_house(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.delete('/users/1/houses/1')
    assert response.status_code == 200
    assert 'House deleted successfully' in response.get_data(as_text=True)

def test_create_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    response = client.post('/users/1/houses/1/rooms', json=room_info)
    assert response.status_code == 201
    response_data = response.get_data(as_text=True)
    assert 'Room created:' in response_data
    assert 'My Dorm' in response_data

def test_get_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.get('/users/1/houses/1/rooms/1')
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'Room found:' in response_data
    assert 'My Dorm' in response_data

def test_update_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    updated_room_info = {'name': 'New Dorm', 'floor': '10', 'size': '300 sq ft'}
    response = client.put('/users/1/houses/1/rooms/1', json=updated_room_info)
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'Room updated:' in response_data
    assert 'New Dorm' in response_data

def test_delete_room(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.delete('/users/1/houses/1/rooms/1')
    assert response.status_code == 200
    assert 'Room deleted successfully' in response.get_data(as_text=True)

def test_create_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    response = client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    assert response.status_code == 201
    response_data = response.get_data(as_text=True)
    assert 'Device created:' in response_data
    assert 'Smart Light' in response_data

def test_get_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    response = client.get('/users/1/houses/1/rooms/1/devices/1')
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'Device found:' in response_data
    assert 'Smart Light' in response_data

def test_update_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    updated_device_info = {'name': 'Smart Thermostat'}
    response = client.put('/users/1/houses/1/rooms/1/devices/1', json=updated_device_info)
    assert response.status_code == 200
    response_data = response.get_data(as_text=True)
    assert 'Device updated:' in response_data
    assert 'Smart Thermostat' in response_data

def test_delete_device(client):
    client.post('/users', json=user_info)
    client.post('/users/1/houses', json=house_info)
    client.post('/users/1/houses/1/rooms', json=room_info)
    client.post('/users/1/houses/1/rooms/1/devices', json=device_info)
    response = client.delete('/users/1/houses/1/rooms/1/devices/1')
    assert response.status_code == 200
    assert 'Device deleted successfully' in response.get_data(as_text=True)

if __name__ == '__main__':
    pytest.main()