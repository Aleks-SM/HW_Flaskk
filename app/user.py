from sqlalchemy.exc import IntegrityError
from flask import views, request, jsonify
from flask_bcrypt import Bcrypt


from app.models import User
from app.error import HttpError
from app.models import Session
# from tools import validate_json
# from schema import CreateUser, UpdateUser


# bcrypt = Bcrypt(app)

def get_user(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, 'User not found')
    return user

def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, 'User already exists')


class UserView(views.MethodView):
    @property
    def session(self):
        return request.session()

    def get(self, user_id: int):
        user = get_user(user_id)
        return jsonify(user.dict)

    def post(self):
        user_data = validate_json(CreateUser, request.json)
        user_data = user_data['password'] = hash_password(user_data['password'])
        user = User(**user_data)
        add_user(user)
        return jsonify({'id': user.id})

    def patch(self, user_id: int):
        user = get_user(user_id)
        user_data = validate_json(UpdateUser, request.json)
        if 'password' in user_data:
            user_data['password'] = hash_password(user_data['password'])
        for key, value in user_data.items():
            setattr(user, key, value)
            add_user(user)
        return jsonify({'id': user.id})

    def delete(self, user_id: int):
        user = get_user(user_id)
        self.session.delete(user_id)
        self.session.commit()
        return jsonify({"status": 'ok'})
