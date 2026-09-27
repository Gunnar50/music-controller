from http import HTTPStatus


def test_warmup(test_client):
  response = test_client.get('/_ah/warmup')
  assert response.status_code == HTTPStatus.OK
