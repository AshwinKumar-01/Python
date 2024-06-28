# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:49:08 2024

@author: ashkg
"""
import math

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        fact=1
        while(n>=1):
            fact*=n
            n-=1
        return fact

def number_to_log10(n):
    return math.log10(n)

def degrees_to_radians(n):
    return n*(math.pi/180)

def find_trignometry(n):
    n=n*(math.pi/180)
    return ("sin value :", math.sin(n),"cos value :", math.cos(n),"tan value: ", math.tan(n))

