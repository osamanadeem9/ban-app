from typing import Optional
from helpers.redis import RedisHelper
import logging

class FailedOrdersMonitor:
    def __init__(self):
        helper = RedisHelper()
        self.redis_client = helper.client
        self.expiration_time = 60 * 60 * 24
        self.logger = logging.getLogger(__name__)

    def add_attempt(self, link):
        key = f"failed_attempts:{link}"
        self.redis_client.incr(key)
        self.logger.info(f"add_attempt: {key}")
        self.redis_client.expire(key, self.expiration_time) 

    def get_attempts(self, link):
        key = f"failed_attempts:{link}"
        self.logger.info(f"get_attempts: {key}")
        return int(self.redis_client.get(key) or 0)

    def reset_attempts(self, link):
        key = f"failed_attempts:{link}"
        self.redis_client.delete(key)
