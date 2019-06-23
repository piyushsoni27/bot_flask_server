#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:24:54 2019

@author: piyush
"""

from nmt import model, params, vocab
from nmt_utils import string_to_int
import numpy as np
from keras.utils import to_categorical

def run_examples(model, params, vocab):
    """
    Run through predefined examples to check model perofrmance.
    """
    
    print("Running examples...\n")
    
    s0 = np.zeros((params['m'], params['n_s']))
    c0 = np.zeros((params['m'], params['n_s']))
    
    EXAMPLES = ['3 May 1979', '5 April 09', '21th of August 2016', 'Tue 10 Jul 2007', 'Saturday May 9 2018', 'March 3 2001', 'March 3rd 2001', '1 March 2001']
    for example in EXAMPLES:
        
        source = string_to_int(example, params['Tx'], vocab['human_vocab'])
        source = np.array(list(map(lambda x: to_categorical(x, num_classes=params['human_vocab_size']), source)))
        source = source.reshape((1, source.shape[0], source.shape[1]))
        prediction = model.predict([source, s0, c0])
        prediction = np.argmax(prediction, axis = -1)
        output = [vocab['inv_machine_vocab'][int(i)] for i in prediction]
        
        print("source:", example)
        print("output:", ''.join(output))
        
    return

run_examples(model, params, vocab)