import flask


def register_routes(flask_app: flask.Flask) -> None:
  from routes import general

  flask_app.register_blueprint(general.ROUTES)


app = flask.Flask(__name__)
register_routes(app)
