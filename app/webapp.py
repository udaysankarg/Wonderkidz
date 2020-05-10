import logging
import os

from flask import (Flask, render_template, abort, request, redirect, url_for)
from model import get_emp_list, dbsetup, insert_emp

logging.basicConfig(filename=os.path.join("results", "app.log"), filemode="w",
                    format='%(asctime)s [%(name)-8s] - %(levelname)-7s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)
logger = logging.getLogger(__name__)


def setup():
    dbsetup()


@app.route('/')
def welcome():
    return render_template(
        "main.html",
        members=["Employees list"]
    )


@app.route('/emplist')
def emp_list():
    try:
        mem = get_emp_list()
        return render_template("member.html",
                               members=mem
                               )
    except IndexError:
        abort(404)


@app.route('/add_member', methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        # form has been submitted, process data
        member = {"fname": request.form['fname'],
                  "lname": request.form['lname'],
                  "gender": request.form['gender'],
                  "dob": request.form['dob'],
                  "doj": request.form['doj'],
                  "type": request.form['type']
                  }
        insert_emp(member)
        logger.info(member)

        return redirect(url_for('emp_list'))
    else:
        return render_template("add_member.html")


if __name__ == '__main__':
    setup()
    logger.critical("I am inside main")
    app.run(host='0.0.0.0', debug=True)
