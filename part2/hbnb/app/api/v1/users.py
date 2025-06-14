from flask_restx import Namespace, Resource
from app.services import facade

api = Namespace('users', description='User operations')

@api.route('/')
class UserList(Resource):
    def get(self):
        users = facade.get_users()
        return [user.to_dict() for user in users], 200
