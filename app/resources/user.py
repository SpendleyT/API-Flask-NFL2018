import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from database.db import users

blp = Blueprint("users", __name__, description="Operations on users.")

@blp.route("/users")
class User(MethodView):
    def get(self):
        return {"users": users}


@blp.route("/user")
class UserCreate(MethodView):
    def post(self):
        user_data = request.get_json()
        user = [user for user in users if user["username"] == user_data["username"]]
        if user:
            abort(500, "That username already exists. Please try another.")

        user_id = uuid.uuid4().hex
        new_user = {
            **user_data,
            "usergroup": "CUSTOMER",
            "user_id": user_id
        }
        users.append(new_user)
        print(users)
        return new_user, 201
