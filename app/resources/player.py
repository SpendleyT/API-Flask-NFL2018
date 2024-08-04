import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from database.db import players


blp = Blueprint("players", __name__, description="Operations on players.")


@blp.route("/player/<string:player_id>")
class Player(MethodView):
    def get(self, player_id):
        try:
            return players[player_id]
        except KeyError:
            abort(404, "Player details not found.")


@blp.route("/players/<string:team_id>")
class PlayerList(MethodView):
    def get(self, team_id):
        try:
            return {k:v for k, v in players.items() if v["team_id"] == team_id}
        except KeyError:
            abort(404, message="Team not found.")   
