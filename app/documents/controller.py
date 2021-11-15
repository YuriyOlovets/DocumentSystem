from flask_restx import Namespace, Resource
from flask import request
import json

from app import cache
from app.utils.auth import bearer_auth_decorator



api = Namespace("DocumentsAPI", description="Information about documents")


@api.route("/")
class MainRoutes(Resource):

    @bearer_auth_decorator
    def get(self):
