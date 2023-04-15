import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError


from database.db import db
from database.models import UserModel
from database.schemas import UserSchema,UserUpdateSchema
from api.user.userController import UserController

user_route = Blueprint("user_route","user_route",description= "Operations on users")
userController = UserController()

@user_route.route("/users")
class UserList(MethodView):
    @user_route.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()
    
    @user_route.arguments(UserUpdateSchema)
    @user_route.response(201, UserSchema)
    def post(self,item_data):
        item = UserModel(**item_data)

        try :
            db.session.add(item)
            db.session.commit()
        except IntegrityError as e:
            abort(400,str(e))
        except SQLAlchemyError:
            abort(505,"An error occurred while creating the item.")
        return item

@user_route.route("/users/<string:user_id>")
class User(MethodView):
    @user_route.response(200,UserSchema)
    def get(self,user_id):
        return UserModel.query.get_or_404(user_id)

    def delete(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"Message": "Item deleted successfully."}

    @user_route.arguments(UserUpdateSchema)
    @user_route.response(201,UserSchema)
    def put(self,user_data,user_id):
        user = UserModel.query.get_or_404(user_id)
        if user:
            user.name = user_data["name"]
            user.age = user_data["age"]
            user.email = user_data["email"]
        else:
            user = UserModel(id = user_id,**user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(505,"An error occurred while creating the item.")
        return user

