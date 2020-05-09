from flask import (Flask, render_template, abort, jsonify, request, redirect, url_for)

import os
import logging

from model import getdbs, get_emp_list

logging.basicConfig(filename=os.path.join("results", "logs.txt"), filemode="w",
                    format='%(asctime)s [%(name)-8s] - %(levelname)-7s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/')
def hello():
    logger.info("I am inside hello")

    return """
    <h1>HELLO Uday4</h1>
    <p>List of DBs</p>
    <table style="width:50%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>Jill</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr>
        <td>Eve</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>
    <p>{}</p>""".format(getdbs())

@app.route('/emplist')
def emp_list():
    return """
    <h2>Emp list</h2>
    <body>{}</body>""".format(get_emp_list())


if __name__ == '__main__':
    logger.critical("I am inside main")
    app.run(host='0.0.0.0', debug=True)
