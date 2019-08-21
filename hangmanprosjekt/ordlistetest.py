#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:42:52 2019

@author: jon
"""

import random as ra
#import string unødvendig

ordListe = open("ordbok", "r").readlines() # Leser inn alle linjene fra tekstfil "ordbok"

antallOrd = len(ordListe) # Length for å finne hvor mange ord i ordboka

selectRandom = ra.randint(0, antallOrd-1) # -1 for å unngå out of bounds, velger et tilfeldig ord fra ordboken

randomWord = ordListe[selectRandom].strip() # strip() for å fjerne trailing space

konvertertilListe = list(randomWord)

print(konvertertilListe)