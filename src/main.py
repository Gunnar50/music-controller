import flask


def register_routes(flask_app: flask.Flask) -> None:
  from api import room as room_apis
  from views import room as room_views

  flask_app.register_blueprint(room_apis.ROUTES)
  flask_app.register_blueprint(room_views.ROUTES)


app = flask.Flask(__name__)
register_routes(app)
