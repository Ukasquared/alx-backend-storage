#!/usr/bin/env python3
""" returns a list from mongo collections"""


def list_all(mongo_collection):
    """returns a list from mongo collections"""
    newlist = []
    for doc in mongo_collection.find():
        newlist.append(doc)
    return newlist
