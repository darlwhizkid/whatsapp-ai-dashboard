import redis
from rq import Queue

class MessageQueue:
    def __init__(self, redis_url: str):
        self.redis_conn = redis.from_url(redis_url)
        self.q = Queue(connection=self.redis_conn)
    
    def enqueue_message(self, message: str, phone_number: str):
        return self.q.enqueue('app.tasks.process_message', message, phone_number)
