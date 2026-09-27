import flask

ROUTES = flask.Blueprint('spotify', __name__, url_prefix='/api/spotify')


@ROUTES.route('/auth', methods=('POST',))
def spotify_auth() -> str:
  return 'ok'


@ROUTES.route('/')
def get_current_song() -> str:
  return 'ok'


@ROUTES.route('/search', methods=('POST',))
def search_song() -> str:
  return 'ok'


@ROUTES.route('/queue', methods=('POST',))
def add_to_queue() -> str:
  return 'ok'


@ROUTES.route('/vote', methods=('POST',))
def vote_to_skip() -> str:
  return 'ok'


@ROUTES.route('/play', methods=('POST',))
def play_song() -> str:
  return 'ok'


@ROUTES.route('/pause', methods=('POST',))
def pause_song() -> str:
  return 'ok'


@ROUTES.route('/skip', methods=('POST',))
def skip_song() -> str:
  return 'ok'
