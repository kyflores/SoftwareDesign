# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:03:42 2014

@author: kyle
"""

def print_left_sect_A():
    print '+ - - - ',
    
    
def print_plus_line():
    do_twice(print_left_sect_A)
    print'+'
    
def print_left_sect_B():
    print '|       ',
    
def print_bar_line():
    do_twice(print_left_sect_B)
    print'|'

def do_twice(function):
    function()
    function()
    
def do_thrice(function):
    function()
    function()
    function()

def do_four_times(function):
    do_twice(function)
    do_twice(function)
    
def make_grid():
    print_plus_line()
    do_four_times(print_bar_line)
    print_plus_line()
    do_four_times(print_bar_line)
    print_plus_line()
    
make_grid()

#This executes but gives an error I don't yet understand.
"""
Exception in thread Thread-1 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 551, in __bootstrap_inner
  File "/usr/lib/python2.7/dist-packages/spyderlib/widgets/externalshell/monitor.py", line 515, in run
  File "/usr/lib/python2.7/dist-packages/spyderlib/widgets/externalshell/monitor.py", line 204, in mglobals
<type 'exceptions.ImportError'>: No module named __main__
"""
#Then when I added this comment it stopped.....