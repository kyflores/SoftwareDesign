# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:40:07 2014

@author: kyle
"""

def fermat(a,b,c,n):
    if(n<=2):
        print'Choose a higher (positive!) value of n!'
    else:
        V=(a^n)+(b^n)-(c^n)
        if(V==0):
            print'Holy Smokes, Fermat was wrong!'
        else:
            print'No, that doesn\'t work...'
            
fermat(3,4,5,3)