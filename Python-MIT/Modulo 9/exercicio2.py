# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:54:05 2017

@author: sey_t
"""

#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#        time = '6:30'
#        print(self.time)
#
#clock = Clock('5:30')
#clock.print_time()

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()