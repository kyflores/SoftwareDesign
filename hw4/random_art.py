# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math

def build_random_function(min_depth, max_depth):
    """
    Takes a minimum and maximum depth input.  The depth corresponds to how many
    recursive calls the function can make, and thus how "deeply" nested a function
    it can make.  Minimum and maximum are specified instead of a particular value
    to increase the randomness of the output.
    
    The available functions are product (two inputs), sine, cosine, x, y, cube,
    and arctangent.
    
    Returns a function as a nested list.
    """
    
    if min_depth<1:
        min_depth=1       
    depth=randint(min_depth,max_depth)         
    if depth==1:
        switch1=randint(1,2)
        if switch1==1:
            return "x"
        elif switch1==2:
            return "y"
    else:
        switch2=randint(0,4)
        if switch2==0:
            return ["prod",build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)]
        elif switch2==1:
            return ["sin_pi",build_random_function(min_depth-1,max_depth-1)]
        elif switch2==2:
            return ["cos_pi",build_random_function(min_depth-1,max_depth-1)]
        elif switch2==3:
            return ["cube",build_random_function(min_depth-1,max_depth-1)]
        elif switch2==4:
            return ["arctan",build_random_function(min_depth-1,max_depth-1)]
        

def evaluate_random_function(f, x, y):
    # your doc string goes here

    length=len(f)
    if length==1: #If the length is one, it's the base case.
        #print(f[0])
        if f[0] == "x":
            return x
        else:
            return y
    elif length==2: #If the length is two, it's anyone of the main operators that isn't product.
        if f[0] == "sin_pi":
            return math.sin(math.pi*evaluate_random_function(f[1],x,y))
        elif f[0] == "cos_pi":
            return math.cos(math.pi*evaluate_random_function(f[1],x,y))
        elif f[0] == "cube":
            return evaluate_random_function(f[1],x,y)**3
        elif f[0] == "arctan":
            return math.atan(evaluate_random_function(f[1],x,y))
    elif length==3: #If the length is 3, it must be product.
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        The function will return the value whose relative position in the new interval is the same
        as the old value's relative position in the old interval.
    """
    return output_interval_start + (float(val)-input_interval_start) * (output_interval_end - output_interval_start) / (input_interval_end - input_interval_start)
    #casts a float on one value to avoid truncating the output if the output is not integer.

def generate_image():    
    R=build_random_function(5,10)
    G=build_random_function(5,10)
    B=build_random_function(5,10)
    im = Image.new("RGB",(350,350))
    for y in range(0,350):
        for x in range(0,350):
            xf=remap_interval(x,0,350,-1,1)            
            yf=remap_interval(y,0,350,-1,1)   
            resR=evaluate_random_function(R,xf,yf)
            resG=evaluate_random_function(G,xf,yf)
            resB=evaluate_random_function(B,xf,yf)
            valR=int(remap_interval(resR,-1,1,1,255))
            valG=int(remap_interval(resG,-1,1,1,255))
            valB=int(remap_interval(resB,-1,1,1,255))
            im.putpixel((x,y),(valR,valG,valB))
    im.show()
    
if __name__=='__main__':
    generate_image()