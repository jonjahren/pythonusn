#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:44:28 2019

@author: jon
"""

flIn1, flIn2, flIn3 = float(input("Tall 1: ")), float(input("Tall 2: ")), float(input("Tall 3: "))
if flIn1 > flIn2 or flIn1 > flIn3:
    print("Første tallet var størst.")
elif flIn2 > flIn1 and flIn2 > flIn3:
    print("Andre tallet er størst.")
elif flIn3 > flIn2 and flIn3 > flIn1:
    print("Det tredje tallet var størst.")
elif flIn1 == flIn2 or flIn1 == flIn3 or flIn2 == flIn3:
    print("Tallene er like.")
else:
    print("Avslutter program.")