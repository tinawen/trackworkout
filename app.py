from flask import Flask, render_template, request, Response, url_for, redirect, flash
from db import records, users
import simplejson
import formencode
import os
from formencode import validators
from functools import wraps

app = Flask(__name__)
app.debug = os.getenv('PORT') is None

@app.route('/records/<person_name>')
def search_records(person_name):
    results_list = []
    if not person_name or person_name == 'all':
        new_records = list(records.find())
        for record in new_records:
            record[u'_id'] = 0
        results_list.extend(new_records)
        results = dict(person_name = 'all',
                       results = results_list,
                       count = len(results_list)
                       )
    else:
        results_list.extend(list(records.find({'person_name': person_name}, {'_id': 0})))
        results = dict(person_name = person_name,
                       results = results_list, 
                       count = len(results_list)
                       )
    return simplejson.dumps(results, indent=4)

@app.route('/add', methods=['POST'])
def add_entry():
    string_validator = validators.String(not_empty=True)
    num_validator = validators.Int(not_empty=True)
    try:
        person_name = string_validator.to_python(request.form['person_name'])
        team = string_validator.to_python(request.form['team'])
        description = string_validator.to_python(request.form['description'])
        duration = num_validator.to_python(request.form['duration'])
        score = num_validator.to_python(request.form['score'])
        date = string_validator.to_python(request.form['date'])
    except formencode.Invalid, e:
        print 'invalid:'
        print e
    else:
        workout = {'person_name': person_name,
                   'team': team,
                   'description': description,
                   'duration': duration,
                   'score': score,
                   'date': date}
        records.insert(workout)
        #flash('New entry was successfully posted')
    return redirect(url_for('index'))

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    result = users.find_one({'person_name': username})

    if result:
        return password == 'wootwoot'
    else:
        return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@requires_auth
def index():
    return render_template('index.html')

@app.route('/foo')
def foo():
    return app.send_static_file('add.html')

if __name__ == '__main__':
    port = os.getenv('PORT')
    if port is not None:
        app.run('0.0.0.0', int(port))
    else:
        app.run()

