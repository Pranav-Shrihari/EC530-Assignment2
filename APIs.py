from flask import Flask, request

app = Flask(__name__)

users = []
houses = []
rooms = []
devices = []

# User methods
def CreateUser(user):
    for u in users:
        if u['id'] == user['id']:
            return None
    users.append(user)
    return user

def ReadUser(id):
    for user in users:
        if user['id'] == id:
            return user
    return None

def UpdateUser(id, user_info):
    for user in users:
        if user['id'] == id:
            user['name'] = user_info['name']
            user['email'] = user_info['email']
            user['phone'] = user_info['phone']
            return user
    return None

def DeleteUser(id):
    for user in users:
        if user['id'] == id:
            users.remove(user)
            return user
    return None

# House methods
def CreateHouse(user_id, house):
    for h in houses:
        if h['id'] == house['id']:
            return None
    house['user_id'] = user_id
    house['room_ids'] = []
    houses.append(house)
    return house

def ReadHouse(user_id, id):
    for house in houses:
        if house['id'] == id:
            return house
    return None

def UpdateHouse(user_id, id, house_info):
    for house in houses:
        if house['id'] == id and house['user_id'] == user_id:
            house['name'] = house_info['name']
            house['address'] = house_info['address']
            return house
    return None

def DeleteHouse(user_id, id):
    for house in houses:
        if house['id'] == id and house['user_id'] == user_id:
            houses.remove(house)
            return house
    return None

# Room methods
def CreateRoom(user_id, house_id, room):
    for r in rooms:
        if r['id'] == room['id']:
            return None
    room['house_id'] = house_id
    room['device_ids'] = []
    rooms.append(room)
    for house in houses:
        if house['id'] == house_id and house['user_id'] == user_id:
            house['room_ids'].append(room['id'])
            return room
    return None

def ReadRoom(user_id, house_id, room_id):
    for room in rooms:
        if room['id'] == room_id and room['house_id'] == house_id:
            for house in houses:
                if house['id'] == house_id and house['user_id'] == user_id:
                    return room
    return None

def UpdateRoom(user_id, house_id, room_id, room_info):
    for room in rooms:
        if room['id'] == room_id and room['house_id'] == house_id:
            for house in houses:
                if house['id'] == house_id and house['user_id'] == user_id:
                    room['name'] = room_info['name']
                    room['floor'] = room_info['floor']
                    room['size'] = room_info['size']
                    return room
    return None

def DeleteRoom(user_id, house_id, room_id):
    for room in rooms:
        if room['id'] == room_id and room['house_id'] == house_id:
            for house in houses:
                if house['id'] == house_id and house['user_id'] == user_id:
                    house['room_ids'].remove(room['id'])
                    rooms.remove(room)
                    return room
    return None

# Device methods
def CreateDevice(user_id, house_id, room_id, device):
    for d in devices:
        if d['id'] == device['id']:
            return None
    device['room_id'] = room_id
    devices.append(device)
    for room in rooms:
        room['device_ids'].append(device['id'])
        if room['id'] == room_id and room['house_id'] == house_id:
            for house in houses:
                if house['id'] == house_id and house['user_id'] == user_id:
                    return device
    return None

def ReadDevice(user_id, house_id, room_id, device_id):
    for device in devices:
        if device['id'] == device_id and device['room_id'] == room_id:
            for room in rooms:
                if room['id'] == room_id and room['house_id'] == house_id:
                    for house in houses:
                        if house['id'] == house_id and house['user_id'] == user_id:
                            return device
    return None

def UpdateDevice(user_id, house_id, room_id, device_id, device_info):
    for device in devices:
        if device['id'] == device_id and device['room_id'] == room_id:
            for room in rooms:
                if room['id'] == room_id and room['house_id'] == house_id:
                    for house in houses:
                        if house['id'] == house_id and house['user_id'] == user_id:
                            device['name'] = device_info['name']
                            return device
    return None

def DeleteDevice(user_id, house_id, room_id, device_id):
    for device in devices:
        if device['id'] == device_id and device['room_id'] == room_id:
            for room in rooms:
                if room['id'] == room_id and room['house_id'] == house_id:
                    for house in houses:
                        if house['id'] == house_id and house['user_id'] == user_id:
                            room['device_ids'].remove(device['id'])
                            devices.remove(device)
                            return device
    return None

# Endpoints
@app.route('/users', methods=['POST'])
def create_user():
    user_info = request.get_json()
    user = CreateUser(user_info)
    if not user:
        return "User already exists\n", 404
    return f"User created: {user}\n", 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = ReadUser(id)
    if not user:
        return "User not found\n", 404
    return f"User found: {user}\n", 200

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_info = request.get_json()
    user = UpdateUser(id, user_info)
    if not user:
        return "User not found\n", 404
    return f"User updated: {user}\n", 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = DeleteUser(id)
    if not user:
        return "User not found\n", 404
    return "User deleted successfully\n", 200

@app.route('/users/<int:user_id>/houses', methods=['POST'])
def create_house(user_id):
    house_info = request.get_json()
    house = CreateHouse(user_id, house_info)
    if not house:
        return "House already exists\n", 404
    return f"House created: {house}\n", 201

@app.route('/users/<int:user_id>/houses/<int:id>', methods=['GET'])
def get_house(user_id, id):
    house = ReadHouse(user_id, id)
    if not house:
        return "House not found\n", 404
    return f"House found: {house}\n", 200

@app.route('/users/<int:user_id>/houses/<int:id>', methods=['PUT'])
def update_house(user_id, id):
    house_info = request.get_json()
    house = UpdateHouse(user_id, id, house_info)
    if not house:
        return "House not found\n", 404
    return f"House updated: {house}\n", 200

@app.route('/users/<int:user_id>/houses/<int:id>', methods=['DELETE'])
def delete_house(user_id, id):
    house = DeleteHouse(user_id, id)
    if not house:
        return "House not found\n", 404
    return "House deleted successfully\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms', methods=['POST'])
def create_room(user_id, house_id):
    room_info = request.get_json()
    room = CreateRoom(user_id, house_id, room_info)
    if not room:
        return "Room already exists or house not found\n", 400
    return f"Room created: {room}\n", 201

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>', methods=['GET'])
def get_room(user_id, house_id, room_id):
    room = ReadRoom(user_id, house_id, room_id)
    if not room:
        return "Room not found\n", 404
    return f"Room found: {room}\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>', methods=['PUT'])
def update_room(user_id, house_id, room_id):
    room_info = request.get_json()
    room = UpdateRoom(user_id, house_id, room_id, room_info)
    if not room:
        return "Room not found\n", 404
    return f"Room updated: {room}\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(user_id, house_id, room_id):
    room = DeleteRoom(user_id, house_id, room_id)
    if not room:
        return "Room not found\n", 404
    return "Room deleted successfully\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>/devices', methods=['POST'])
def create_device(user_id, house_id, room_id):
    device_info = request.get_json()
    device = CreateDevice(user_id, house_id, room_id, device_info)
    if not device:
        return "Device already exists or room not found\n", 400
    return f"Device created: {device}\n", 201

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['GET'])
def get_device(user_id, house_id, room_id, device_id):
    device = ReadDevice(user_id, house_id, room_id, device_id)
    if not device:
        return "Device not found\n", 404
    return f"Device found: {device}\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['PUT'])
def update_device(user_id, house_id, room_id, device_id):
    device_info = request.get_json()
    device = UpdateDevice(user_id, house_id, room_id, device_id, device_info)
    if not device:
        return "Device not found\n", 404
    return f"Device updated: {device}\n", 200

@app.route('/users/<int:user_id>/houses/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['DELETE'])
def delete_device(user_id, house_id, room_id, device_id):
    device = DeleteDevice(user_id, house_id, room_id, device_id)
    if not device:
        return "Device not found\n", 404
    return "Device deleted successfully\n", 200

# Run the server locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)