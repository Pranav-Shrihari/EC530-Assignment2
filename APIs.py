from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory data
users = []
houses = []
rooms = []
devices = []

# Pydantic Models
class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class House(BaseModel):
    id: int
    name: str
    address: str

class Room(BaseModel):
    id: int
    name: str
    floor: int
    size: str

class Device(BaseModel):
    id: int
    name: str

# Utility functions

def find_user(id: int):
    return next((u for u in users if u['id'] == id), None)

def find_house(id: int):
    return next((h for h in houses if h['id'] == id), None)

def find_room(id: int):
    return next((r for r in rooms if r['id'] == id), None)

def find_device(id: int):
    return next((d for d in devices if d['id'] == id), None)

# User Endpoints
@app.post("/users", status_code=201)
def create_user(user: User):
    if find_user(user.id):
        raise HTTPException(status_code=400, detail="User already exists")
    users.append(user.model_dump())
    return user

@app.get("/users/{id}")
def get_user(id: int):
    user = find_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{id}")
def update_user(id: int, user_info: User):
    user = find_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.update(user_info.model_dump())
    return user

@app.delete("/users/{id}")
def delete_user(id: int):
    user = find_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user)
    return {"detail": "User deleted"}

# House Endpoints
@app.post("/users/{user_id}/houses", status_code=201)
def create_house(user_id: int, house: House):
    if find_house(house.id):
        raise HTTPException(status_code=400, detail="House already exists")
    house_data = house.model_dump()
    house_data['user_id'] = user_id
    house_data['room_ids'] = []
    houses.append(house_data)
    return house_data

@app.get("/users/{user_id}/houses/{id}")
def get_house(user_id: int, id: int):
    house = find_house(id)
    if not house or house['user_id'] != user_id:
        raise HTTPException(status_code=404, detail="House not found")
    return house

@app.put("/users/{user_id}/houses/{id}")
def update_house(user_id: int, id: int, house_info: House):
    house = find_house(id)
    if not house or house['user_id'] != user_id:
        raise HTTPException(status_code=404, detail="House not found")
    house.update(house_info.model_dump())
    return house

@app.delete("/users/{user_id}/houses/{id}")
def delete_house(user_id: int, id: int):
    house = find_house(id)
    if not house or house['user_id'] != user_id:
        raise HTTPException(status_code=404, detail="House not found")
    houses.remove(house)
    return {"detail": "House deleted"}

# Room Endpoints
@app.post("/users/{user_id}/houses/{house_id}/rooms", status_code=201)
def create_room(user_id: int, house_id: int, room: Room):
    if find_room(room.id):
        raise HTTPException(status_code=400, detail="Room already exists")
    for house in houses:
        if house['id'] == house_id and house['user_id'] == user_id:
            room_data = room.model_dump()
            room_data['house_id'] = house_id
            room_data['device_ids'] = []
            rooms.append(room_data)
            house['room_ids'].append(room.id)
            return room_data
    raise HTTPException(status_code=404, detail="House not found")

@app.get("/users/{user_id}/houses/{house_id}/rooms/{room_id}")
def get_room(user_id: int, house_id: int, room_id: int):
    room = find_room(room_id)
    if not room or room['house_id'] != house_id:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.put("/users/{user_id}/houses/{house_id}/rooms/{room_id}")
def update_room(user_id: int, house_id: int, room_id: int, room_info: Room):
    room = find_room(room_id)
    if not room or room['house_id'] != house_id:
        raise HTTPException(status_code=404, detail="Room not found")
    room.update(room_info.model_dump())
    return room

@app.delete("/users/{user_id}/houses/{house_id}/rooms/{room_id}")
def delete_room(user_id: int, house_id: int, room_id: int):
    room = find_room(room_id)
    if not room or room['house_id'] != house_id:
        raise HTTPException(status_code=404, detail="Room not found")
    for house in houses:
        if house['id'] == house_id:
            house['room_ids'].remove(room_id)
            rooms.remove(room)
            return {"detail": "Room deleted"}

# Device Endpoints
@app.post("/users/{user_id}/houses/{house_id}/rooms/{room_id}/devices", status_code=201)
def create_device(user_id: int, house_id: int, room_id: int, device: Device):
    if find_device(device.id):
        raise HTTPException(status_code=400, detail="Device already exists")
    for room in rooms:
        if room['id'] == room_id and room['house_id'] == house_id:
            device_data = device.model_dump()
            device_data['room_id'] = room_id
            devices.append(device_data)
            room['device_ids'].append(device.id)
            return device_data
    raise HTTPException(status_code=404, detail="Room not found")

@app.get("/users/{user_id}/houses/{house_id}/rooms/{room_id}/devices/{device_id}")
def get_device(user_id: int, house_id: int, room_id: int, device_id: int):
    device = find_device(device_id)
    if not device or device['room_id'] != room_id:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.put("/users/{user_id}/houses/{house_id}/rooms/{room_id}/devices/{device_id}")
def update_device(user_id: int, house_id: int, room_id: int, device_id: int, device_info: Device):
    device = find_device(device_id)
    if not device or device['room_id'] != room_id:
        raise HTTPException(status_code=404, detail="Device not found")
    device.update(device_info.model_dump())
    return device

@app.delete("/users/{user_id}/houses/{house_id}/rooms/{room_id}/devices/{device_id}")
def delete_device(user_id: int, house_id: int, room_id: int, device_id: int):
    device = find_device(device_id)
    if not device or device['room_id'] != room_id:
        raise HTTPException(status_code=404, detail="Device not found")
    for room in rooms:
        if room['id'] == room_id:
            room['device_ids'].remove(device_id)
            devices.remove(device)
            return {"detail": "Device deleted"}