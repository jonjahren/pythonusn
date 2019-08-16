#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 08:52:41 2019

@author: jon
"""
import random as ra

randNry, randNrx = ra.randint(10, 100), ra.randint(10, 100)

gangeStykke = randNry * randNrx
minusStykke = randNry - randNrx
plusStykke = randNry + randNrx
riktigeSvar = 0
feilSvar = 0

print("Hva er resultatet av ", randNry, "*", randNrx, "?")

svarMult = int(input())

if svarMult == gangeStykke:
    print("Det var riktig svar! \n")
    riktigeSvar = riktigeSvar + 1
elif svarMult != gangeStykke:
    print("Det var feil svar! \n")
    feilSvar = feilSvar + 1
    
print("Hva er resultatet av ", randNry, "-", randNrx, "?")

svarMinus = int(input())

if svarMinus == minusStykke:
    print("Det var riktig svar! \n")
    riktigeSvar = riktigeSvar + 1
elif svarMinus != minusStykke:
    print("Det var feil svar! \n")
    feilSvar = feilSvar + 1

    
    
print("Hva er resultatet av ", randNry, "+", randNrx, "?")

svarPluss = int(input())

if svarPluss == plusStykke:
    print("Det var riktig svar! \n")
    riktigeSvar = riktigeSvar + 1
elif svarPluss != plusStykke:
    print("Det var feil svar! \n")
    feilSvar = feilSvar + 1
    
print("Du har ", riktigeSvar, "riktige svar og ", feilSvar, "feil svar.")