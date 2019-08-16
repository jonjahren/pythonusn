#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:57:57 2019

@author: jon
"""

import random

tilfeldigTall = random.randint(1, 10)


while True:
    gjetteTall = int(input("Gjett et tall: "))
    if gjetteTall == tilfeldigTall:
        print("Du gjettet riktig!")
        break
    elif gjetteTall != tilfeldigTall:
        print("Prøv igjen")
            
    