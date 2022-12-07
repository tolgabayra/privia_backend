from mongoengine import Document, StringField,BooleanField



class Comment(Document):
    text = StringField(required=True)
    user_id = StringField()
    topic_id = StringField()
    is_active = BooleanField(default=True)