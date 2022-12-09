import os
from flask import make_response, request


import jwt

def verify_authorization(func):
    secret = os.environ.get('TOKEN_SECRET')
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['token']
        except Exception as e:
            return make_response({"message": "Token not provided"}, 403)
        
        try:
            user =  jwt.decode(token, secret, algorithms=["HS256"])
            print(user)
            return func(*args, **kwargs)
        except Exception as e:
            return make_response({"message": "Invalid token provided"}, 403)   
    return wrapper