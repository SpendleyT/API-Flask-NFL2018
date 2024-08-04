from flask.views import MethodView
from flask_smorest import Blueprint, abort
from database.db import games


blp = Blueprint("games", __name__, description="Operations on games.")


@blp.route("/game/<string:game_id>")
class Game(MethodView):
    def get(self, game_id):
        try:
            return games[game_id]
        except KeyError:
            abort(404, message="Team not found.")


@blp.route("/games/<string:team_id>")
class TeamGame(MethodView):
    def get(self, team_id):
        try:
            return {k:v for k, v in games.items() if v["team_id"] == team_id}
        except KeyError:
            abort(404, message="Team not found.")


@blp.route("/games")
class GameList(MethodView):
    def get(self):
        return {"games": games}
    
