from flask import Blueprint
from src.models.user import User

users_blueprint = Blueprint('users', __name__,
                            template_folder='../templates/users')