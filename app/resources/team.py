import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from database.db import teams


blp = Blueprint("teams", __name__, description="Operations on teams.")


@blp.route("/team/<string:team_id>")
class Team(MethodView):
    def get(self, team_id):
        try:
            return teams[team_id]
        except KeyError:
            abort(404, message="Team not found.")


@blp.route("/teams")
class TeamList(MethodView):
    def get(self):
        return {"teams": teams}
    

