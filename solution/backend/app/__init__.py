from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
UPLOAD_FOLDER = './app/uploads'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    objects = db.relationship('Object', backref='image', lazy='dynamic')


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    x_min = db.Column(db.Integer)
    y_min = db.Column(db.Integer)
    x_max = db.Column(db.Integer)
    y_max = db.Column(db.Integer)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))


from app import routes


