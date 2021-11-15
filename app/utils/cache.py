from redis import Redis

class Cache:
    def __init__(self, redis_connection: Redis):
        from app import env
        self.env = env
        self.redis = redis_connection

    def set(self, key: str, value: str, timeout=3600):
        return self.redis.set(key, value, timeout)

    def get(self, key: str):
        return self.redis.get(key)

    def delete(self, key: str):
        return self.redis.delete(key)