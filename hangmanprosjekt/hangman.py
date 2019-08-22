#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

dictionary_list = open("ordbok", "r").readlines() # Leser inn alle linjene fra tekstfil "ordbok"

word_count = len(dictionary_list) # Length for å finne hvor mange ord i ordboka

select_random = ra.randint(0, word_count-1) # -1 for å unngå out of bounds, velger et tilfeldig ord tall

# strip() fjerner trailing whitespace, og dette bruker det tilfeldiget tallet for å 
# velge et ord fra ordlisten

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
guesses = 0
input_letter = [] # Må defineres før while()

# Denne for-løkken populerer gjetteordet med underscores

for i in range(len(random_word_to_list)):
    guess_word.append("_")


# alfabetLower = list(string.ascii_lowercase) overflødig
# alfabetUpper = list(string.ascii_uppercase) overflødig


print(random_word)
print(guess_word)

while True:
    print("Tast bokstav for å gjette:")
    
    index_number = [] # Denne variabelen lagrer hvilken index bokstavene er i
    input_letter = input() # Dette blir en string. 
    input_to_list = list(input_letter) # Konverterer string til liste
    
    print(used_letters, input_to_list, ''.join(guess_word)) # Debug-print
    
    ######################################################
    #                                                    #
    #  Finner hvilken plassering bokstavene er i listen  #
    #                                                    #
    #                                                    #
    ######################################################    
    
    for index in range(len(random_word_to_list)):
        print(random_word_to_list, index, input_letter)
        if random_word_to_list[index] == input_letter:
            index_number.append(index)
            print(random_word_to_list[index], input_letter)
    
    #######################################################
    #                                                     #
    # Disse to if-setningene tester om bokstaven finnes   #
    # i listen over brukte bokstaver. Om den ikke finnes  #
    # så blir den lagt til i listen. Om den finnes så     #
    # gir programmet beskjed.                             #
    #                                                     #
    #######################################################
    
    if index_number:
        print("Bokstaven finnes i ordet.")
        if input_letter in used_letters:
            print("Duplikatbokstav.")
        else:
            used_letters.append(input_letter)
            
            
    if not index_number:
        print("Bokstaven er ikke der.")
        if input_letter not in used_letters:
            used_letters.append(input_letter)
    
    ######################################################
    # Denne for-løkken plasserer riktige bokstaver i     #
    # listen slik at vi kan konstruere løsningsordet.    #
    ######################################################
    
    for index in index_number:
        guess_word[index] = input_letter
    
    #######################################################
    # if-setningen gjør om ordene til strenger og         #
    # sammenligner dem. Om de er like så avsluttes spillet#
    #######################################################
    
    
    if ''.join(random_word_to_list) == ''.join(guess_word):
        print("Du vant! Løsningsordet var:", ''.join(guess_word))
        break
    
    # Enkel if-setning for å avslutte spillet om det er for mange forsøk
    
    if guesses >= max_guesses:
        print("Du har brukt for mange forsøk, mannen ble hengt.")
    
    guesses = guesses + 1
    print(random_word_to_list)
    print(guess_word)
    print(used_letters)

