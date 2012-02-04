from pymongo import Connection
import os

mongo_uri = os.getenv('MONGOLAB_URI')
if mongo_uri is None:
    mongo_uri = 'mongodb://localhost:27017/test_database'

connection = Connection(mongo_uri)
db = connection.test_database
records = db.workouts
users = db.users
