#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:20:03 2019

@author: jon
"""

# import math
from datetime import date

# Triks!
alderFloat, forNavn, etterNavn  = float(input("Alder: ")), input("Fornavn: "), input("Etternavn: ")
birthYear, turningFifty = date.today().year - int(alderFloat), int(date.today().year) - int(alderFloat) + 50 # Femti her er et 'magisk tall fordi det er oppgitt i oppgaven


# Utskrift
print("Navnet ditt er: ", forNavn, etterNavn, "og du er ", int(alderFloat), "år gammel. Du ble født ca. ", birthYear, "og du fyller femti ca. ", turningFifty)
