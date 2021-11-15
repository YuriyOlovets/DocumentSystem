from flask import request
from app import env
from redis import Redis


def bearer_auth_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        if env.ENABLE_AUTH is False:
            return func(*args, **kwargs)

        if request.headers.get('authorization'):
            redis_conn = Redis(host=env.CRM_REDIS_HOST,
                               port=env.CRM_REDIS_PORT,
                               password=env.CRM_REDIS_PASSWORD)
            if redis_conn.get(request.headers.get('authorization').lower().replace('bearer ', '')) is not None:
                return func(*args, **kwargs)
        return {"msg": "unauthorized"}, 401
    return wrapper