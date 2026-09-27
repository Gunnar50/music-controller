import flask

ROUTES = flask.Blueprint('routes', __name__)


@ROUTES.route('/_ah/warmup')
def warmup():
  return 'Ok'
