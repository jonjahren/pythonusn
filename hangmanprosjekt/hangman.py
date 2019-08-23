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
lose_count_messages = len(lose_messages)
dup_messages_length = len(duplicate_messages)
tries_messages_length = len(tries_messages)

# -1 for å unngå out of bounds, velger et tilfeldig ord fra ordboken

select_random = ra.randint(0, word_count-1)
select_random_lose = ra.randint(0, lose_count_messages-1)
select_random_dup_messages = ra.randint(0, dup_messages_length-1)
select_random_tries = ra.randint(0, tries_messages_length-1) 

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
guesses = 0 # Hvor mange ganger du har gjettet på en bokstav
input_letter = [] # Må defineres før while()

# Denne for-løkken populerer gjetteordet med underscores

for i in range(len(random_word_to_list)):
    guess_word.append("_")


# alfabetLower = list(string.ascii_lowercase) overflødig
# alfabetUpper = list(string.ascii_uppercase) overflødig

while True:
    print("Velkommen til hangman, ordet du skal gjette er", len(random_word), "tegn langt")
    
    index_number = [] # Denne variabelen lagrer hvilken index bokstavene er i
    input_letter = input() # Dette blir en string. 
    input_to_list = list(input_letter) # Konverterer string til liste
    
    #print(used_letters, input_to_list, ''.join(guess_word)) # Debug-print
    
    ######################################################
    #                                                    #
    #  Finner hvilken plassering bokstavene er i listen  #
    #                                                    #
    #                                                    #
    ######################################################    
    
    for index in range(len(random_word_to_list)):
        #print(random_word_to_list, index, input_letter) <- Debug print
        if random_word_to_list[index].casefold() == input_letter.casefold():
            index_number.append(index)
            #print(random_word_to_list[index], input_letter) <- debug print
    
    #######################################################
    #                                                     #
    # Disse to if-setningene tester om bokstaven finnes   #
    # i listen over brukte bokstaver. Om den ikke finnes  #
    # så blir den lagt til i listen. Om den finnes så     #
    # gir programmet beskjed.                             #
    #                                                     #
    #######################################################
    
    if index_number:
        select_random_tries = ra.randint(0, tries_messages_length-1) 
        random_guess_message = tries_messages[select_random_tries].strip()
        print(random_guess_message)
        if input_letter in used_letters:
            select_random_dup_messages = ra.randint(0, dup_messages_length-1)
            duplicate_message_try = duplicate_messages[select_random_dup_messages].strip()
            print(duplicate_message_try)
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
    
    if ''.join(random_word_to_list).casefold() == ''.join(guess_word).casefold():
        print("Du vant! Løsningsordet var:", ''.join(guess_word))
        break
    
    # Enkel if-setning for å avslutte spillet om det er for mange forsøk
    
    if guesses >= max_guesses:
        select_random_lose = ra.randint(0, lose_count_messages-1)
        random_lose_message = lose_messages[select_random_lose].strip()
        print(random_lose_message, "og det trivielle ordet du skulle finne var:", ''.join(random_word_to_list))
        break
    
    guesses = guesses + 1
    used_letters.sort()
    print(guess_word)
    print(used_letters)

