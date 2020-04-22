#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
from flask import escape
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states():
    """Displays states"""
    state_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    """Removes current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
