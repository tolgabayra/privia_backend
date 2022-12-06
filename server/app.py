import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from mongoengine import connect

from routes.auth import auth_route
from routes.topic import topic_route
from routes.comment import comment_route

app = Flask(__name__)
app.register_blueprint(auth_route)
app.register_blueprint(topic_route)
app.register_blueprint(comment_route)



CORS(app)
load_dotenv()

connect(username='root', password='root', db='mongodb')




