#!/usr/bin/env python3
"""inserts a new document
in a collection """


def insert_school(mongo_collection, **kwargs):
    """inserts a new
    document in a collection"""
    mongo_collection.insert_one({**kwargs})
    new_id = mongo_collection.find().sort("_id", -1).limit(1).next()
    return new_id['_id']
