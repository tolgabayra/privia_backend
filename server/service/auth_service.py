from model.user import User
from flask import make_response

def signup_service(userdata):
    try:
        email_check = User.objects[:1](email=userdata['email'])
        if email_check:
            return {"status": 404, "message": "email already exists"}
        else:
            username = userdata['username']
            password = userdata['password']

            new_user = User(username=username, password=password)

            new_user.save()
            return make_response({'message': 'User succesfully created'}, 200)

    except Exception as e:
        return make_response({'message': str(e)}, 404)


def login_service(user_credentials):
    try:
        email_check = User.objects[:1](email=user_credentials['email'])
        if not email_check:
            return {"status": 404, "message": "email does not exists"}
        else:
            for user in email_check:

