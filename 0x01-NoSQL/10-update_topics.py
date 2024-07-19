#!/usr/bin/env python3
"""changes all topics of a
school document based
on the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a
    school document based
    on the name"""
    # update the name using the update method
    # then set the topic using the same update
    # method
    mongo_collection.update_many(
        { 'name': name },
        { "$set": {"topics": topics} }
    )
