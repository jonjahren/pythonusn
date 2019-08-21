#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:12:29 2019

@author: jon
"""

import random as ra

dictionary_list = open("ordbok", "r").readlines() # Leser inn alle linjene fra tekstfil "ordbok"

word_count = len(dictionary_list) # Length for å finne hvor mange ord i ordboka

select_random = ra.randint(0, word_count-1) # -1 for å unngå out of bounds, velger et tilfeldig ord tall

# strip() fjerner trailing whitespace, og dette bruker det tilfeldiget tallet for å 
# velge et ord fra ordlisten
random_word = dictionary_list[select_random].strip()

random_word_to_list = list(random_word) # Gjør om tilfeldig ord fra streng til liste
guess_word = [] # Denne variabelen lagrer hvilket ord som blir gjettet
max_tries = 0 # Hvor mange forsøk man har brukt
used_letters = [] # Hvilke bokstaver som er brukt
input_to_list= [] # Denne er lagret for å gjøre om input streng til liste

# Denne for-løkken populerer gjetteordet med underscores
for i in range(len(random_word_to_list)):
    guess_word.append("_")


# alfabetLower = list(string.ascii_lowercase) overflødig
# alfabetUpper = list(string.ascii_uppercase) overflødig

input_letter = [] # Må defineres før while()
print(random_word)
print(guess_word)

while True:
    print("Tast bokstav for å gjette:")
    index_number = [] # Denne variabelen lagrer hvilken index bokstavene er i
    input_letter = input() # Dette blir en string. 
    input_to_list = list(input_letter) # Konverterer string til liste
    
    print(used_letters, input_to_list, ''.join(guess_word)) # Debug-print
    
    
    ####################################################
    # Denne for-løkken skal finne ut om ordet ikke     #
    # finnes i ordet, og legge til bokstaven som ble   #
    # brukt for til å gjette.                          #
    #                                                  # 
    ####################################################

            
    
    ######################################################
    #  Finner hvilken plassering bokstavene er i listen  #
    #                                                    #
    ######################################################    
    
    for index in range(len(random_word_to_list)):
        if random_word_to_list[index] == input_letter:
            index_number.append(index)
            print(random_word_to_list[index])
            if random_word_to_list[index] != input_letter:
                print("bokstaven er ikke i ordet")
            else:
                print("bokstaven er i ordet")
    
    ######################################################
    # Denne for-løkken plasserer riktige bokstaver i     #
    # listen slik at vi kan konstruere løsningsordet.    #
    ######################################################
    
    for index in index_number:
        guess_word[index] = input_letter
    
    if ''.join(random_word_to_list) == ''.join(guess_word):
        print("Du vant! Løsningsordet var:", ''.join(guess_word))
        break
    
    print(random_word_to_list)
    print(guess_word)
    print(used_letters)