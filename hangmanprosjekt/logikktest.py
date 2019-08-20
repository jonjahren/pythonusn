#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:03:37 2019

@author: jon
"""

import random as ra

ordListe = open("ordbok", "r").readlines() # Leser inn alle linjene fra tekstfil "ordbok"

antallOrd = len(ordListe) # Length for å finne hvor mange ord i ordboka

selectRandom = ra.randint(0, antallOrd-1) # -1 for å unngå out of bounds

randomWord = ordListe[selectRandom].strip() # strip() for å fjerne trailing space

antallForsøk = 0 # Hvor mange forsøk man har brukt
forsøkBokstaver = []
forsøkAlfabet = []

inputWord = " " # Må defineres før while()

print(randomWord)

while randomWord != inputWord:
    print("Tast bokstav for å gjette:" )
    inputWord = input()
    if antallForsøk >= 12:
        print("Mannen ble hengt.")
        break
    if inputWord in randomWord:
        antallForsøk = antallForsøk + 1
        print("Den bokstaven er i ordet.")
        print("Du har brukt: ", antallForsøk, " forsøk. Du har ", 13 - antallForsøk, "igjen.")
        
    elif inputWord not in randomWord:
        antallForsøk = antallForsøk + 1
        print("Bokstaven er ikke i ordet.")
        print("Du har brukt: ", antallForsøk, " forsøk. Du har ", 12 - antallForsøk, "igjen.")
