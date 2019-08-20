#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:25:21 2019

@author: jon
"""
import random as ra
"""

Vi åpner ordbokfilen med read-only i parametrene til wordDict fordi vi bare skal
hente ut variabler, ikke modifisere filen. readlines() funsjonen henter ut
en spesifikk linje. Husk at index starter på 0, så readlines()[0] blir det
første ordet i linja.

"""

ordListe = open("ordbok", "r").readlines()

antallOrd = len(ordListe)

selectRandom = ra.randint(0, antallOrd-1)


"""
Vi må bruke .strip for å fjerne whitespace som legger seg etter ordet når man
importerer de fra ordboklisten.
"""
randomWord = ordListe[selectRandom].strip()



while True:
    print(randomWord)
    print("Tast inn en bokstav for å gjette ordet:")
    testInput = input()
    
    if testInput == randomWord: 
        print("Success! Avslutter...")
        break
    if len(testInput) == 2:
        print("Tast inn en bokstav av gangen.")
    elif len(testInput) == len(randomWord) and testInput == randomWord:
        print("Det var riktig ord! Gratulerer!")
    elif testInput != randomWord:
        print("Feil ord. Mannen blir hengt.")
        break
        
"""
Hvis du ikke konverterer variabelen i i denne for-løkken, så blir den en
string, og da kan du ikke sjekke indexen av string med den.

"""

"""
for i in range(len(randomWord)):
    if testInput == randomWord[i]:
        print("Bokstaven finnes")
        break
    else:
        print("Dette finnes ikke i ordet")
"""
