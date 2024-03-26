#!/usr/bin/env python3
"""Python function that changes topics of a
school docu based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name will be the school name to update
topics will be the list of topics approached
in the school
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """changes to school docu"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
