"""Flask configs for development mode"""

# Apply all settings that deployed versions use
from prod_server_with_shared.prod_server.settings import *  # noqa: F403

DEBUG = True
TESTING = True

# So running tests doesn't try to get config from datastore
SECRET_KEY = 'some-random-words'
