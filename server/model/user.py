from mongoengine import Document, StringField, EmailField

class User(Document):
    username = StringField(required=True, max_length=256)
    password = StringField(required=True, max_length=1024)