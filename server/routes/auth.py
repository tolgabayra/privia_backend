from flask import request,jsonify, Blueprint
from service.auth_service import login_service, signup_service

auth_route = Blueprint('user_route', __name__)


@auth_route.route("/api/v1/auth/login", methods=['POST'])
def login_user():
    data = request.get_json()
    return login_service(data)


@auth_route.route("/api/v1/auth/register", methods=['POST'])
def signup_user():
    data = request.get_json()
    return signup_service(data) 