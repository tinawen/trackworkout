from datetime import date
from db import records
from db import users

def load_data():
    records.remove() #load from scratch
    users.remove()

    user1 = {'person_name': 'tina',
            'team': 'power through'
            }

    user2 = {'person_name': 'eric',
            'team': 'power through'
            }

    user3 = {'person_name': 'karyn',
            'team': 'schuchmans'
            }

    user4 = {'person_name': 'tina',
            'team': 'schuchmans'
            }

    users.insert(user1)
    users.insert(user2)
    users.insert(user3)
    users.insert(user4)

    workout1 = {'person_name': 'tina',
                'team': 'power through',
                'description': 'ultimate frisbee',
                'duration': 120,
                'date': date.today().strftime("%A %d, %B %Y"),
                'score': 100}

    workout2 = {'person_name': 'eric',
                'team': 'power through',
                'description': 'running',
                'duration': 40,
                'date':date.today().strftime("%A %d, %B %Y"),
                'score': 100}

    workout3 = {'person_name': 'karyn',
                'team': 'schuchmans',
                'description': 'swimming',
                'duration': 60,
                'date':date.today().strftime("%A %d, %B %Y"),
                'score': 90}

    workout4 = {'person_name': 'tina',
                'team': 'power through',
                'description': 'Dance Central',
                'duration': '60',
                'date':date.today().strftime("%A %d, %B %Y"),
                'score': 60}

    records.insert(workout1)
    records.insert(workout2)
    records.insert(workout3)
    records.insert(workout4)
    print 'data loading done'

if __name__ == '__main__':
    load_data()
