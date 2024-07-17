#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from typing import Union
import uuid

class Cache:
    """writing strings to redis"""
    def __init__(self):
        """ create an instance of redis """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, int,
              bytes, float]) -> str:
        """ store string to redis db"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id    
