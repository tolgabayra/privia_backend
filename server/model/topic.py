from mongoengine import Document, StringField,BooleanField, ListField,EmbeddedDocumentField
from model import comment

class Topic(Document):
    title = StringField(required=True, max_length=256)
    desc = StringField(required=True, max_length=256)
    user_id = StringField()
    comments = ListField()
    no_comment = BooleanField(default=True)