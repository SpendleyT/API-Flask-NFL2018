from flask import Flask
from flask_smorest import Api

from resources.team import blp as TeamBlueprint
from resources.player import blp as PlayerBlueprint
from resources.user import blp as UserBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)


api.register_blueprint(TeamBlueprint)
api.register_blueprint(PlayerBlueprint)
api.register_blueprint(UserBlueprint)

