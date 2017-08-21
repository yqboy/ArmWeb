# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
from sysinfo import getInfo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/io', methods=['post'])
def getIO():
    return jsonify({'ret': 0, 'msg': getInfo()})


if __name__ == '__main__':
    app.run()
