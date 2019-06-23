#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:42:16 2019

@author: piyush
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        input_string = str(request.form.get('message'))
        return jsonify(input_string)
    else:
        return render_template('index.html')

@app.route('/')         #root directory(homepage)
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)