# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:38:24 2014

@author: kyle

"""

from random_art import *
if __name__=='__main__':
    R=build_random_function(2,4)
    print(R)
    print(evaluate_random_function(R, 0.1, 0.5))