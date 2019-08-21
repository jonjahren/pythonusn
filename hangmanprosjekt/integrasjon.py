#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:24:21 2019

@author: jon
"""

import numpy as np

def trapes_int(f, a, b, n):
    total = 0
    bredde = (b -a) / n
    
    #trapes0 = (f(a) + f(a + bredde)) / 2 * bredde
    #trapes1 = (f(a + bredde) + f(a + bredde + bredde)) / 2 * bredde
    #trapes2 = (f(a + bredde + bredde) + f(a + bredde + bredde + bredde)) / 2 * bredde
    
    #trapesx = (f(a + x * bredde) + f(a + (x + 1) * bredde)) / 2 * bredde
    
    for x in range(n):
        total += (f(a + x * bredde) + f(a + (x + 1) * bredde)) / 2 * bredde
        
    return total

def f1(x):
    return x**5

def f1_int(x):
    return x**6 / 6

def exact(f, a, b):
    return f(b) - f(a)

svar = trapes_int(f1, 0, 5, 250)

riktig_svar = exact(f1_int, 0, 5)
print(riktig_svar)
print(svar)