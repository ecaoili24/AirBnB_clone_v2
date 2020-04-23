#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask, render_template, escape
from models import storage, State, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def show_filters():
    """Displays states, cities, and amenities under filters"""
    state_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', state_dict=state_dict,
                           amenity_dict=amenity_dict)


@app.teardown_appcontext
def teardown_db(self):
    """Removes current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
