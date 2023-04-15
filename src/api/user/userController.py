from database.models import UserModel
from database.db import db

class UserController:
    def get_users(self):
        return UserModel.query.all()