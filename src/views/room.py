import flask

ROUTES = flask.Blueprint('room_views', __name__, url_prefix='/')


def generate_code(lenght=5) -> str:
  return 'ABCDE'


@ROUTES.route('/')
def index() -> str:
  # Check if user is already in a room (flask session)
  # if is in a room, redirect to the room
  # otherwise redirect to create room page
  return 'ok'


@ROUTES.route('/<string:room_code>')
def room(room_code: str) -> str:
  return 'ok'


@ROUTES.route('/create')
def create_room() -> str:
  return flask.render_template('create.html')
