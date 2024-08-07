import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from database.database import DatabaseConnection


blp = Blueprint("users", __name__, description="Operations on users.")

@blp.route("/users")
class User(MethodView):
    def get(self):
        users = DatabaseConnection.get_all_users()
        return {"users": users}


@blp.route("/user")
class UserCreate(MethodView):
    def post(self):
        user_data = request.get_json()
        user = DatabaseConnection.get_user_by_id(user_data.user_id)
        if user:
            abort(500, "That username already exists. Please try another.")

        user_id = uuid.uuid4().hex
        new_user = {
            **user_data,
            "usergroup": "CUSTOMER",
            "user_id": user_id
        }
        DatabaseConnection.add_user(new_user)
        return new_user, 201
