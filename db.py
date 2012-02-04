from pymongo import Connection

connection = Connection()
db = connection['test_database']
records = db.workouts
users = db.users
