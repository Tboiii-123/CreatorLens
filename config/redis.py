import os
import redis
from decouple import config

REDIS_URL = config("REDIS_URL")

redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)