import os

from flask import Flask
from flask_restx import Api
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_cors import CORS
from redis import Redis
from app.utils.cache import Cache

from app.config import config_by_name


env = os.getenv("ENVIRONMENT") if os.getenv("ENVIRONMENT") is not None else 'dev'
env = config_by_name[env]

redis_conn = Redis(host=env.CACHE_HOST, port=env.CACHE_PORT, decode_responses=True)
cache = Cache(redis_conn)


def create_app():
    from app.routes import register_routes
    global env

    app = Flask(__name__)

    CORS(app)

    api = Api(app, title="User API", version="0.1.0")
    register_routes(api, app)


    return app
