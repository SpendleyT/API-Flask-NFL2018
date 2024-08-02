import uuid
from flask import Flask, request
from database.db import users, players, teams


app = Flask(__name__)


@app.get("/teams")
def get_all_teams():
    return {"teams": teams}


@app.get("/team/<string:team_id>")
def get_team(team_id):
    try:
        return teams[team_id]
    except KeyError:
        return {"message": "Team not found."}, 404
    

@app.get("/players/<string:team_id>")
def get_players_for_team(team_id):
    try:
        return players[team_id]
    except KeyError:
        return {"message": "Team not found."}, 404


@app.get("/player/<string:player_id>")
def get_player_by_id(player_id):
    pass


@app.get("/plays/<string:team>/<string:date>")
def get_plays_for_game(team, date):
    pass


@app.get("/users")
def get_all_users():
    return {"users": users}


@app.post("/user")
def create_new_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    new_user = {
        **user_data,
        "usergroup": "CUSTOMER",
        "user_id": user_id
    }
    users[user_id] = new_user
    print(users)
    return new_user, 201

