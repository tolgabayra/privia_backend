from flask import request, Blueprint
from service.topic_service import create_service, delete_service, update_service, list_service, list_all_service
topic_route = Blueprint('topic_route', __name__)

@topic_route.route("/api/v1/topic", methods=['POST'])
def create_topic():
    data = request.get_json()
    return create_service(data)
    

@topic_route.route("/api/v1/topic/<topic_id>", methods=['DELETE'])
def delete_topic(topic_id):
    return delete_service(topic_id)
    

@topic_route.route("/api/v1/topic/<topic_id>", methods=['PUT'])
def update_topic(topic_id):
    topic_data = request.get_json()
    return update_service(topic_id, topic_data)
    

@topic_route.route("/api/v1/topic", methods=['GET'])
def get_topic():
    return list_service()
    
@topic_route.route("/api/v1/topics", methods=['GET'])
def get_all_topic():
     return list_all_service()
