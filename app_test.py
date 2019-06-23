#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:42:16 2019

@author: piyush
"""

from flask import Flask, render_template, request, jsonify

from nmt import pred
from nmt_utils import string_to_int
import numpy as np
from keras.utils import to_categorical

app = Flask(__name__)
print(pred("3 May 1979"))
"""
def predict(input_string):
    source = string_to_int(input_string, params['Tx'], vocab['human_vocab'])
    source = np.array(list(map(lambda x: to_categorical(x, num_classes=params['human_vocab_size']), source)))
    source = source.reshape((1, source.shape[0], source.shape[1]))
    prediction = model.predict([source, s0, c0])
    prediction = np.argmax(prediction, axis = -1)
    output = [vocab['inv_machine_vocab'][int(i)] for i in prediction]
    return ''.join(output)

#
"""

@app.route('/prediction_in/<input_str>', methods=['GET', 'POST'])
def prediction_in(input_str):
    print("method : {}".format(request.method))
    input_string = str(input_str)
    print("Input: {}\n".format(input_string))
    prediction = str(pred(input_string))
    print("prediction: {}\n".format(prediction))
    return jsonify(prediction)


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        input_string = str(request.args.get('message'))
        print("Input: {}\n".format(input_string))
        prediction = str(pred(input_string))
        print("prediction: {}\n".format(prediction))
        return jsonify(prediction)
    else:
        return render_template('index.html')

@app.route('/')         #root directory(homepage)
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)

