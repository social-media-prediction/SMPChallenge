#-*-coding:utf-8-*-

from flask import Flask, render_template, request
import os
import time
import os
import numpy as np

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/challenge', methods=['GET'])
def challenge():
    return render_template('challenge.html')

@app.route('/download', methods=['GET'])
def download():
    return render_template('download.html')

@app.route('/dataset', methods=['GET'])
def dataset():
    return render_template('dataset.html')


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('leaderboard.html')
    

if __name__ == '__main__':
    app.run('127.0.0.1', 8000, threaded=True)
