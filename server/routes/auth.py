from flask import request,jsonify, Blueprint
auth_route = Blueprint('user_route', __name__)


@auth_route.route("/api/v1/auth/register", methods=['POST'])
def login_user():
    data = request.get_json()
    return jsonify(data)