from typing import Optional, List, Dict
from helpers.redis import RedisHelper

class FailedAttemptsMonitor:
    def __init__(self):
        helper = RedisHelper()
        self.redis_client = helper.client
        self.expiration_time = 60 * 60 * 24  # 1 day

    def record_failed_attempt(self, user_id: Optional[str] = None, 
                              email: Optional[str] = None, 
                              ip: Optional[str] = None) -> None:
        """Record a failed order attempt with the provided identifiers."""
        if user_id:
            self._increment_attempt(f"user_id:{user_id}")
        if email:
            self._increment_attempt(f"email:{email}")
        if ip:
            self._increment_attempt(f"ip:{ip}")

    def _increment_attempt(self, key: str) -> None:
        """Increment the failed attempt count for a specific key."""
        self.redis_client.incr(key)
        self.redis_client.expire(key, self.expiration_time)

    def get_recent_failed_attempts(self, user_id: Optional[str] = None, 
                                   email: Optional[str] = None, 
                                   ip: Optional[str] = None) -> List[Dict]:
        """Get recent failed order attempts for a user/email/IP."""
        attempts = []
        if user_id:
            attempts.append(self._get_attempts(f"user_id:{user_id}"))
        if email:
            attempts.append(self._get_attempts(f"email:{email}"))
        if ip:
            attempts.append(self._get_attempts(f"ip:{ip}"))
        return attempts

    def _get_attempts(self, key: str) -> Dict:
        """Get the number of failed attempts for a specific key."""
        count = int(self.redis_client.get(key) or 0)
        return {"key": key, "attempts": count}

