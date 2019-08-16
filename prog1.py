"""
Import er for å importere pakker for å utvide funksjonaliteten til python
"""

import math
import random

"""

Variabler blir tilordnet.
Det kan være en fordel å gi variabler korte men beskrivende navn, og camelcase
bør være standard. e.g: minVariabel

"""

side1Firkant = 3
side2Firkant = 4
heiStreng1 = "Hei"
heiStreng2 = "Verden"


"""

Print skriver output til stdout. Standard er konsolloutput.
Det er også en god ide å gjøre det slik at print() blir minst mulig fylt med
uttrykk. Om print blir veldig lang, lag en funksjon for å utføre jobben.

"""


print(2 * 3 - 4 / 2 * 2)
print( (1-3) * -3 / (2*2))
print(2*3**2/2)
print(0.5**3 - 4 - 8 / 2* 4)
print(2**3 - (4-8) / 2 * 4)

b = 12
a = 3
print(a * b)

a = 4
b = 5
print(a*2 + b*2)

print(3.14*3**2)

b = "7.3"
a = "30.1"

#flytb = float(b)
#flyta = float(a)

differanse = float(b) - float(a)

summen = float(b) + float(a)

produktet = float(b) * float(a)

produkt2 = round(produktet,1)

print("Differansen er ", differanse, "summen er ", summen, "produktet er ", produkt2)

a = 3.14
b = "Pi er "

astreng = str(a)

c = b + astreng

print(c)

radianer = math.radians(90)
cosinusGrader = math.cos(90)
cosinusRadianer = math.cos(radianer)

print(cosinusGrader, "\n", cosinusRadianer)

nullOgen = random.random()
randomTall1 = random.uniform(-5, 5)
randomTall2 = random.uniform(-2, 18)

print(nullOgen, " ", randomTall1, " ", randomTall2)
