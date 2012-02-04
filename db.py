from pymongo import Connection
import os
from urlparse import urlparse

mongo_uri = os.getenv('MONGOLAB_URI')
if mongo_uri is None:
    mongo_uri = 'mongodb://localhost:27017/test_database'

connection = Connection(mongo_uri)
db = connection[urlparse(mongo_uri).path[1:]]
records = db.workouts
users = db.users

