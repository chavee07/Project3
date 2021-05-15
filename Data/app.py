import pandas as pd
import sqlite3
from sqlalchemy.orm import Session

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# # Read sqlite query results into a pandas DataFrame
# con = sqlite3.connect("../data/project2.sqlite")
# df = pd.read_sql_query("SELECT * from WorldHappiness", con)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/landing<br/>"
    )


@app.route("/api/v1.0/landing")
def names():
    # Create our session (link) from Python to the DB

    """Return a list of all passenger names"""
    # Query all passengers
    con = sqlite3.connect("../data/project2.sqlite")
    test_run = pd.read_sql_query("SELECT * from WorldHappiness", con)



    print(test_run)

    # Convert list of tuples into normal list
    all_names = test_run.to_json()

    return jsonify(all_names)

if __name__ == '__main__':
    app.run(debug=True)