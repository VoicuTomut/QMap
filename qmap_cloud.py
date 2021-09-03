import sys

import json

# Make sure flask is installed
from flask import request
from flask import jsonify
from flask import make_response
from flask import Flask
from flask import render_template

from qmap_api import clasic_Brut

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Start "

@app.route("/clasicBrut")
def clasicBrut():
    file = request.files['jsonfile']
    poz = json.load(file)
    print(poz)
    return 0



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# http://127.0.0.1:8008/execute_qiskit?circuit_file=GROVER-14-14.qpf
# http://127.0.0.1:8008/do_qiskit_test
