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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states_and_cities(id=None):
    """Displays states and cities by state id"""
    state_dict = storage.all(State)
    found = None
    if id is not None:
        for state in state_dict.values():
            if state.id == id:
                found = state
    return render_template('9-states.html', state_dict=state_dict, id=id,
                           found=found)


@app.teardown_appcontext
def teardown_db(self):
    """Removes current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
