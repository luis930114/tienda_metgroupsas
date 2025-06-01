from flask import request
from flask_jwt_extended import create_access_token
from models.user import UserModel

def register():
    data = request.get_json()
    if UserModel.find_by_username(data['username']):
        return {"message": "User already exists."}, 400
    UserModel.register(data['username'], data['password'])
    return {"message": "User created successfully."}, 201

def auth():
    data = request.get_json()
    user = UserModel.find_by_username(data['username'])
    if user and user.verify_password(data['password']):
        token = create_access_token(identity=str(user.id))
        return {"access_token": token}
    return {"message": "Invalid credentials"}, 401
