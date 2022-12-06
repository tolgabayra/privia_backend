from mongoengine import Document, StringField, EmailField



class Comment(Document):
    text = StringField(required=True)
    user_id = StringField()
    topic_id = StringField()