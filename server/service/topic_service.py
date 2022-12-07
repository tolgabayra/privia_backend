from model.topic import Topic
from flask import make_response
from utils.jwt_token import validate_token


@validate_token
def create_service(data):
    try:
        title = data['title']
        desc = data['dsc']
        user_id = data['user_id']

        new_topic = Topic(title=title, desc=desc, user_id=user_id)

        new_topic.save()
        return make_response({'message': 'Topic successfully created'})

    except Exception as e:
        return make_response({'message': str(e)}, 404)

@validate_token
def delete_service(topic_id):
    try:
        topic = Topic.objects(id=topic_id)
        if topic:
            topic.delete()

            return make_response({'message' : 'Succesfully delected'}, 200)   
        else:
            return make_response({'message' : 'Topic does not exists'}, 404)   

    except Exception as e:
        return make_response({'message' : str(e)}, 404)   


def update_service(topic_id, topic_data):
    try:
        topic = Topic.objects(_id = topic_id)
        if topic:
            topic = topic.get(_id = topic_id)
            topic.title = topic_data['title']
            topic.desc = topic_data['desc']
            topic.user_id = topic_data['user_id']
            topic.save()
            return make_response({'message' : 'Succesfully updated'},202)   
        
        else:
            return make_response({'message' : "Topic does not exists"}, 404) 
    except Exception as e:
        return make_response({'message' : str(e)}, 404)   


def list_service(user_id):
    topics = []
    for topic in Topic.objects:
        topic_data = {}
        if  topic_data['_id'] == user_id:
            
            topic_data['_id'] = str(topic.id)
            topic_data['title'] = str(topic.title)
            topic_data['desc'] = str(topic.desc)
            topic_data['user_id'] = str(topic.user_id)
            topics.append(topics)

            return make_response({'topics': topics}, 200)

        else:
            return make_response({'message' : 'You can not view'},403)   


def list_all_service():
    topics = []
    try:
        for topic in Topic.objects:
            topic_data = {}
            topic_data['_id'] = str(topic.id)
            topic_data['title'] = str(topic.title)
            topic_data['desc'] = str(topic.desc)
            topics.append(topic_data)

        return {"topics": topics}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  



       
    