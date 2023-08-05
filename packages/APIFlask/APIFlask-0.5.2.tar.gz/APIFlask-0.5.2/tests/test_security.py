from apiflask import APIFlask
from apiflask import auth_required
from apiflask.security import HTTPTokenAuth
from apiflask.security import HTTPBasicAuth


def test_default_auth_error_handler(app, client):
    auth = HTTPTokenAuth()

    @app.route('/foo')
    @auth_required(auth)
    def foo():
        pass

    rv = client.get('/foo')
    assert rv.status_code == 401
    assert rv.headers['Content-Type'] == 'application/json'
    assert 'message' in rv.json
    assert rv.json['message'] == 'Unauthorized'
    assert 'WWW-Authenticate' in rv.headers


def test_bypasss_default_auth_error_handler():
    app = APIFlask(__name__, json_errors=False)
    auth = HTTPTokenAuth()

    @app.route('/foo')
    @auth_required(auth)
    def foo():
        pass

    rv = app.test_client().get('/foo')
    assert rv.status_code == 401
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert b'Unauthorized Access' in rv.data
    assert 'WWW-Authenticate' in rv.headers


def test_current_user_as_property(app, client):
    auth = HTTPBasicAuth()

    @auth.verify_password
    def verify_password(username, password):
        if username == 'foo' and password == 'bar':
            return {'user': 'foo'}

    @app.route('/foo')
    @auth_required(auth)
    def foo():
        return auth.current_user

    rv = client.get('/foo', headers={'Authorization': 'Basic Zm9vOmJhcg=='})
    assert rv.status_code == 200
    assert rv.json == {'user': 'foo'}
