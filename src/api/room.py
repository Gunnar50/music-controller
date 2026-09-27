import flask
import werkzeug

from utils import api
from utils import flask_helpers
from utils import models

ROUTES = flask.Blueprint('room_apis', __name__, url_prefix='/api/room')


def generate_code(lenght=5) -> str:
  return 'ABCDE'


@ROUTES.route('/', methods=('POST',))
def create_room() -> werkzeug.Response:
  room_code = generate_code()
  room = models.Room(room_code=room_code)
  room.put()
  return flask.redirect(flask.url_for('room', code=room_code))


@ROUTES.route('/<string:room_code>', methods=('POST',))
def join_room():
  code = flask.request.args.get('code', '').upper()

  request, _ = flask_helpers.get_parameters(api.JoinRoomRequest)

  if not request.code:
    return flask.render_template(
      'join.html', code=code, error='Please enter a room code.'
    )

  room = models.Room.get_by_code(code)
  if not room:
    return flask.render_template(
      'join.html', code=code, error='Room not found.'
    )

  room.put()

  return flask.redirect(flask.url_for('room', code=code))


@ROUTES.route('/<string:room_code>/leave', methods=('POST',))
def leave_room():
  return 'ok'


@ROUTES.route('/<string:room_code>', methods=('PUT',))
def update_room():
  return 'ok'


@ROUTES.route('/<string:room_code>/users', methods=('PUT',))
def get_users():
  return 'ok'
