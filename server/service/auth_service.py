from model.user import User
from flask import make_response
from utils.password_encryption import encrypt_password, compare_passwords
from utils.jwt_token import generate_token
import datetime

def signup_service(userdata):
    try:
        username_check = User.objects[:1](username=userdata['username'])
        print(userdata)
        if username_check:
            return {"status": 404, "message": "Username already exists"}
        else:
            username = userdata['username']
            password = encrypt_password(userdata['password'])

            new_user = User(username=username, password=password)

            new_user.save()
            return make_response({'message': 'User succesfully created'}, 201)

    except Exception as e:
        return make_response({'message': str(e)}, 404)


def login_service(user_credentials):
    try:
        username_check = User.objects[:1](username=user_credentials['username'])
        if not username_check:
            return {"status": 404, "message": "Username does not exists"}
        else:
            for user in username_check:
                payload = {"username": user['username'], "_id": str(user['id']), 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(minutes=60)}
                if compare_passwords(user_credentials['password'], user['password']):
                    token = generate_token(payload, "SecretKey")
                    result = make_response({'token': token}, 200)
                    result.set_cookie('token', token, httponly=True)
                    return result
                else:
                    return make_response({'message': 'Invalid password'}, 403)
    except Exception as e:
        print(e)
        return make_response({'message': str(e)}, 404)
