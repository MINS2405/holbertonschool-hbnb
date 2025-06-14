from flask_restx import Api
from flask import Blueprint
from .v1 import users_ns

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)
api.add_namespace(users_ns)
