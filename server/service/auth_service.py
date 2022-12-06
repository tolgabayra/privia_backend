from model.user import User
from flask import make_response
from utils.password_encryption import encrypt_password, compare_passwords
from utils.jwt_token import generate_token
import datetime

def signup_service(userdata):
    try:
        email_check = User.objects[:1](email=userdata['email'])
        if email_check:
            return {"status": 404, "message": "email already exists"}
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
        email_check = User.objects[:1](email=user_credentials['email'])
        if not email_check:
            return {"status": 404, "message": "email does not exists"}
        else:
            for user in email_check:
                payload = {"email": user['email'], "_id": str(user['id']), 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(minutes=60)}
                if compare_passwords(user_credentials['password'], user['password']):
                    token = generate_token(payload, "SecretKey")
                    return make_response({'token': token}, 200)
                else:
                    return make_response({'message': 'Invalid password'}, 403)
    except Exception as e:
        return make_response({'message': str(e)}, 404)
