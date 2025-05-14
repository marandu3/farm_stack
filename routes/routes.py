from fastapi import APIRouter
from model.model import User
from serializer.serializer import convertdatas
endpoints = APIRouter()
from config import farmcollection as Users
from bson import ObjectId


@endpoints.get("/")
async def read_root():
    return {"Hello": "World"}

#post users
@endpoints.post("/users")
async def create_user(user: User):
    user_data = user.model_dump()
    user_data["_id"] = str(ObjectId())  # Optional: add custom ID
    Users.insert_one(user_data)
    return {"status": "success", "data": user_data}

#get users
@endpoints.get("/users")
async def get_users():
    users = Users.find()
    converted_users = convertdatas(users)
    return {
        'status': "success",
        "data": converted_users
    }
