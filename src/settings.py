# Allow CSRF token to be used in API calls from Javascript
CSRF_COOKIE_HTTPONLY = False

NONE = "'none'"
SELF = "'self'"
DATA = 'data:'

# Start with strict
CSP_POLICY = {
  'default-src': [NONE],
  'connect-src': [SELF],
  'img-src': [SELF],
  'script-src': [SELF],
  'style-src': [SELF],
}
