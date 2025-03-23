import redis

class RedisHelper:
    def __init__(self, host='redis', port=6379):
        self.client = redis.StrictRedis(host=host, port=port, decode_responses=True)

    def set_value(self, key, value):
        self.client.set(key, value)

    def get_value(self, key):
        return self.client.get(key)