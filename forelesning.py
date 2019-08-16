#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:40:25 2019

@author: jon
"""

import random as ra

antallSeksere = 0
antallFemmere = 0

for i in range(5):
    tall = ra.randint(1,6)
    #print("Kast nummer ", i, ":", tall)    
    if tall == 6:
        antallSeksere = antallSeksere + 1
    if tall == 5:
        antallFemmere = antallFemmere + 1