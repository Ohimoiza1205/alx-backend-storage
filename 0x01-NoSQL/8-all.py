#!/usr/bin/env python3
"""Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no doc in the collection
mongo_collection will be the pymongo collection object
"""


import pymongo


def list_all(mongo_collection):
    """Returns docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
