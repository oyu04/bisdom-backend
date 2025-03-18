from flask import Flask
from flask_cors import CORS  # CORSをインポート
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
#from chat import chat_function,chat_test

app = Flask(__name__)
app.config.from_object("config")
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)
