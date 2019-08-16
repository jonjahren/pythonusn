#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:48:00 2019

@author: jon
"""

import random as ra

# Dette populerer en liste med tilfeldige terningkast mellom 1 og 6
tkList = [ra.randint(1,6), ra.randint(1,6), ra.randint(1,6)]

print(tkList[0], tkList[1], tkList[2])

"""
Av en eller annen årsak så blir if-setningene helt merkelige når jeg bare bruker
or/and. I and-setningen så må jeg inkludere alt jeg sammenligner
f.eks var1 == var3 and var4 fungerer ikke. Derimot, om jeg sammenligner på denne måten:
if var1 == var3 and var1 == var4 <- Dette fungerer som det skal.
"""

if tkList[0] == tkList[1] and tkList[0] == tkList[2]:
    print("Det er 3 like terningkast.")
elif tkList[0] == tkList[1] or tkList[0] == tkList[2] or tkList[1] == tkList[2]:
    print("Det er 2 like terningkast.")

if tkList[0] != tkList[1] and tkList[0] != tkList[2] and tkList[1] != tkList[2]:
    print("Det er ingen like kast.")
    