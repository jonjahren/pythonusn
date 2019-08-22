#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####################################################
# Variabler får navn etter C-konvensjon.           #
# eks. om det er logisk med 2 ord så får vi en     #
# underscore: variable_name                        #
#                                                  #
# Løkker får en ny linje mellomrom ned til ny      #
# løkke.                                           #
#                                                  #
#                                                  #
####################################################

import random as ra

#################################################
# Leser inn meldinger til spiller og ordene man # 
# skal gjette.                                  #
#################################################

dictionary_list = open("ordbok", "r").readlines()
lose_messages = open("lost", "r").readlines()
duplicate_messages = open("duplicates", "r").readlines()
tries_messages = open("tries", "r").readlines()

# Length for å finne hvor mange ord i ordboka

word_count = len(dictionary_list) 

# -1 for å unngå out of bounds, velger et tilfeldig ord fra ordboken

select_random = ra.randint(0, word_count-1) 

####################################################
# Når man importerer tekst med readlines()         #
# så får man en \n inkludert på slutten av alle    #
# ordene. For å fjerne evt. mellomrom i starten    #
# og på slutten av alle ordene så kan vi benytte   #
# en innebygget funksjon i python som heter strip()#
####################################################

random_word = dictionary_list[select_random].strip()

####################################################
#                                                  #
# vi setter bare opp noen variabler vi trenger.    #
#                                                  #
####################################################

random_word_to_list = list(random_word) # Gjør om tilfeldig ord fra streng til liste
guess_word = [] # Denne variabelen lagrer hvilket ord som blir gjettet
max_guesses = 12 # Hvor mange forsøk man har brukt
used_letters = [] # Hvilke bokstaver som er brukt
input_to_list= [] # Denne er lagret for å gjøre om input streng til liste
guesses = 0 # Hvor mange ganger du har gjettet på en bokstav
input_letter = ""

# Denne for-løkken populerer gjetteordet med underscores

for i in range(len(random_word_to_list)):
    guess_word.append("_")

print(random_word)
print(guess_word)
input_letter = input("Yo")    


###############################################
#                                             #
# Funksjon for å nullstille spill.            #
# Bruk av 'global' er litt hacky fordi lokale #
# variabler modifiserer ikke globale          #
#                                             #
###############################################

def reset_game():
    global random_word_to_list, guess_word, max_guesses, used_letters, input_to_list, guesses, random_word
    select_random = ra.randint(0, word_count-1)
    random_word = dictionary_list[select_random].strip()
    random_word_to_list = list(random_word) 
    guess_word = [] 
    max_guesses = 12 
    used_letters = [] 
    input_to_list= [] 
    guesses = 0
    
###########################################
# Funksjon som returnerer hvilke plasser  #
# bokstav-input finnes på                 #
#                                         #
###########################################

def find_placement(string_to_find):
    index_number = []
    for index in range(len(random_word_to_list)):
        if random_word_to_list[index] == string_to_find:
            index_number.append(index)
            return index_number
            print(index_number)
        else:
            return False
            print(index_number)            

##########################################################
# Funksjon som undersøker om bokstaven finnes i ordet,   #
# og deretter legger bokstaven til i listen over         #
# bokstaver som er brukt. Varsler om bokstaven allerede  #
# har vært benyttet.                                     #
##########################################################      

def check_input():
    if find_placement:
        print("Denne bokstaven finnes i ordet")
        if input_letter in used_letters:
            print("Men denne bokstaven er allerede brukt")
        else:
            used_letters.append(input_letter)
    if not find_placement:
        print("Denne bokstaven finnes ikke i ordet")
        if input_letter not in used_letters:
            used_letters.append(input_letter)            


find_placement(input_letter)
check_input()
print(used_letters)