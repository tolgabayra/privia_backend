from flask import request, Blueprint
from service.comment_service import create_service, delete_service, update_service, list_service
comment_route = Blueprint('comment_route', __name__)

@comment_route.route("/api/v1/comment", methods=['POST'])
def create_comment():
    data = request.get_json()
    return create_service(data)
    

@comment_route.route("/api/v1/comment/<comment_id>", methods=['DELETE'])
def delete_comment(comment_id):
    return delete_service(comment_id)
    

@comment_route.route("/api/v1/comment/<comment_id>", methods=['PUT'])
def update_comment(comment_id):
    comment_data = request.get_json()
    return update_service(comment_id, comment_data)
    

@comment_route.route("/api/v1/comment", methods=['GET'])
def get_comment():
    return list_service()
    