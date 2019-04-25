from src import db
from sqlalchemy.orm import relationship, backref
from flask_security import UserMixin, RoleMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))


class Role(RoleMixin, db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(UserMixin, db.Model):
    """
        User model
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean())
    roles = relationship('Role', secondary='roles_users', backref=backref('users', lazy='dynamic'))

    def __repr__(self):
        return f"user id: {self.id}, user email: {self.email}"


class OAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = 'oauth'

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User)
