#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:04:12 2019

@author: jon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:03:37 2019

@author: jon
"""

import random as ra
#import string unødvendig

ordListe = open("ordbok", "r").readlines() # Leser inn alle linjene fra tekstfil "ordbok"

antallOrd = len(ordListe) # Length for å finne hvor mange ord i ordboka

selectRandom = ra.randint(0, antallOrd-1) # -1 for å unngå out of bounds, velger et tilfeldig ord tall

# strip() fjerner trailing whitespace, og dette bruker det tilfeldiget tallet for å 
# velge et ord fra ordlisten
randomWord = ordListe[selectRandom].strip()

konvList = list(randomWord)

antallForsøk = 0 # Hvor mange forsøk man har brukt
nyliste = []
listLetters = []

# alfabetLower = list(string.ascii_lowercase) overflødig
# alfabetUpper = list(string.ascii_uppercase) overflødig

inputLetters = [] # Må defineres før while()

print(randomWord)

while konvList != inputLetters:
    
    
    if inputLetters not in nyliste:
        nyliste = nyliste + listLetters # Legger til bokstaver som er brukt
    
    print(nyliste)

    nyliste.sort # Sorterer de alfabetisk
    
    print("Tast bokstav for å gjette:" )
    inputLetters = input()
    listLetters = list(inputLetters)
    
    if inputLetters == "Quit":
        print("Hadetbra")
        break
    
    if antallForsøk >= 12:
        print("Mannen ble hengt.")
        break
    
    if inputLetters in nyliste:
        print("Den bokstaven er brukt.")
        continue # Dette sender oss tilbake til toppen av løkken
    
    if inputLetters in randomWord:
        antallForsøk = antallForsøk + 1
        nyliste = nyliste.append([inputLetters])
        print("Den bokstaven er i ordet.")
        print("Du har brukt: ", antallForsøk, " forsøk. Du har ", 13 - antallForsøk, "igjen.")
        print("Disse boktavene er brukt", nyliste)
        
    elif inputLetters not in randomWord:
        antallForsøk = antallForsøk + 1
        print("Bokstaven er ikke i ordet.")
        print("Du har brukt: ", antallForsøk, " forsøk. Du har ", 12 - antallForsøk, "igjen.")