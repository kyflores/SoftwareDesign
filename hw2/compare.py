# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:58:35 2014

@author: kyle
"""


def compare(x,y):
    #return 1 if x>y
    #return 0 if x=y
    #return -1 if x<y.
    a=x-y
    if (a==0):
        return 0
    else:
        return a/(abs(a))
        
print compare(8,2)