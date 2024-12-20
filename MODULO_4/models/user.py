from database import db
from flask_login import UserMixin
from sqlalchemy import Column, String

class User(db.Model, UserMixin):
    # ID (int), Username (text), password (text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')