from model.comment import Comment
from flask import make_response



def create_service(data):
    try:
        title = data['title']
        desc = data['desc']
        user_id = data['user_id']

        new_comment = Comment(title=title, desc=desc, user_id=user_id)

        new_comment.save()
        return make_response({'message': 'comment successfully created'})

    except Exception as e:
        return make_response({'message': str(e)}, 404)


def delete_service(comment_id):
    try:
        comment = Comment.objects(id=comment_id)
        if comment:
            comment.delete()

            return make_response({'message' : 'Succesfully delected'}, 200)   
        else:
            return make_response({'message' : 'comment does not exists'}, 404)   

    except Exception as e:
        return make_response({'message' : str(e)}, 404)   


def update_service(comment_id, comment_data):
    try:
        comment = Comment.objects(_id = comment_id)
        if comment:
            comment = comment.get(_id = comment_id)
            comment.title = comment_data['title']
            comment.desc = comment_data['desc']
            comment.user_id = comment_data['user_id']
            comment.save()
            return make_response({'message' : 'Succesfully updated'},202)   
        
        else:
            return make_response({'message' : "comment does not exists"}, 404) 
    except Exception as e:
        return make_response({'message' : str(e)}, 404)   


def list_service(user_id):
    comments = []
    for comment in Comment.objects:
        comment_data = {}
        if  comment_data['_id'] == user_id:
            
            comment_data['_id'] = str(comment.id)
            comment_data['title'] = str(comment.title)
            comment_data['desc'] = str(comment.desc)
            comment_data['user_id'] = str(comment.user_id)
            comments.append(comments)

            return make_response({'comments': comments}, 200)

        else:
            return make_response({'message' : 'You can not view'},403)   


       
    