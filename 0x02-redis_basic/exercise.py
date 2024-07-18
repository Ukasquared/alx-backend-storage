#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from typing import Union, Callable
import uuid

class Cache:
    """writing strings to redis"""
    def __init__(self):
        """ create an instance of redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int,
              bytes, float]) -> str:
        """ store string to redis db"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str,
            fn: Callable = None) -> Union[str, float, int, bytes]:
        """ get value from the database"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """convert to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: int) -> int:
        """convert to int"""
        return self.get(key, int(lambda x: x.decode('utf-8')))
