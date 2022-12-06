from mongoengine import Document, StringField, EmailField, BooleanField

class User(Document):
    username = StringField(required=True, max_length=256)
    password = StringField(required=True, max_length=1024)
    is_admin = BooleanField(default=False)