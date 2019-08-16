#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:07:57 2019

@author: jon
"""

import math

# Utregning med grader og ikke radianer
sinGrader = math.sin(35)
cosGrader = math.cos(35)

# Konvertering fra grader til radianer
radianConv = math.radians(35)

# Utregning med radianer
sinRad = math.sin(sinGrader)
cosRad = math.cos(sinGrader)

# Kvadrater
sinKvad = sinGrader**2
cosKvad = cosGrader**2

# Utskrift av utregning
print("Radianer: ", sinRad, " ", cosRad, "\n")
print("Grader: ", sinKvad, cosKvad, cosKvad+sinKvad, "\n")


# Fra radianer til grader
cosGrader, sinGrader = math.cos(math.degrees(2.3)), math.sin(math.degrees(2.3))

#Utskrift av utregning
print("Grader: ", sinGrader, cosGrader, "\n")

# Kvadratrot
print(math.sqrt(256))

inputNum = float(input("Oppgi et tall: "))

squareInput, piMult = round(math.sqrt(inputNum), 2), round(math.pi*inputNum, 0)

print(squareInput, piMult)

