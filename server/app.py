import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from mongoengine import connect

from routes.auth import auth_route


app = Flask(__name__)
app.register_blueprint(auth_route)


CORS(app)
load_dotenv()

connect(username='root', password='root', db='mongodb')




