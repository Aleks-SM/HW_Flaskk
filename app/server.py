from error import HttpError
from models import Session, User

import flask
import jsonify
import requests



# app = flask.Flask("app")

@app.before_request
def before_request():
    session = Session()
    requests.session = session

@app.after_request
def after_request(response: flask.Response):
    requests.session.close()
    return response


@app.errorhandler(HttpError)
def error_handler(HttpError):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response