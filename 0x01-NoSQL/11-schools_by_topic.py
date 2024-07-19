#!/usr/bin/env python3
"""that returns the list of
school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """that returns the list of
    school having a specific topic
    """
    # find the topic in the collection
    document = mongo_collection.find({"topics":
        {"$regex": f"^{topic}"}}
    )
    return document
