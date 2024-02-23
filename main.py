import flask
from flask import request

from app.models import Session
from app.app import create_app
from app.user import UserView

app = create_app()

def before_request():
    session = Session()
    request.session = session

def after_request(response: flask.Response):
    request.session.close()
    return response


def user_view1():
    return {'message': 'Run Flask'}

user_view = UserView.as_view('user')

app.add_url_rule('/', view_func=user_view1)
app.add_url_rule('/user/<int:user_id>', view_func=user_view, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)