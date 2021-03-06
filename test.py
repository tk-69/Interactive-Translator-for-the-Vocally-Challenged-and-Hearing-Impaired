from flask import Flask

from db import db_init
from sqlalchemy import create_engine
#engine = create_engine('sqlite:///sales.db', echo = True)

app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'