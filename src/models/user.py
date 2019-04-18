from src import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """
        User model
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, name="", avatar="", tokens=""):
        self.email = email
        self.name = name
        self.avatar = avatar
        self.tokens = tokens

    def __repr__(self):
        return f"user id: {self.id}, user email: {self.email}"