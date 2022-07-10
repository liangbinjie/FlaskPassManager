from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    passwords = db.relationship('Passwords', backref='admin')


class Passwords(db.Model):
    id = db.Column(db.Integer, primary__key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    email = db.Column(db.String(200))
    username = db.Column(db.String(100))
