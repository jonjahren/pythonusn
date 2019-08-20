#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:16:41 2019

@author: jon
"""

import numpy as np
import matplotlib.pyplot as plt

def pos(t, v0, a=0):
    s = v0 * t + 0.5 * a * t**2
    return s

plt.ion()
akse = plt.axes(xlim = (0,150), ylim = (0,40))

vx0 = 10
vy0 = 10

dt = 0.1
t = 0

ay = -9.18

x = 0
y = 0
plt.pause(3)
while y >= 0:
    x = pos(t, vx0)
    y = pos(t, vy0, ay)
    akse.scatter([x], [y], c="r")
    t = t + dt
    plt.pause(dt)




"""
antBiler = 700
lengder = np.random.uniform(3.5, 6, antBiler)
akselerasjon = np.random.uniform(4, 12, antBiler)
colors = np.random.rand(antBiler)
areal = np.pi * (15 * np.random.rand(antBiler))**2

#plt.plot(lengder, akselerasjon, ".b")

plt.scatter(lengder, akselerasjon, s = areal, c = colors, alpha = 0.5)
plt.xlabel("Billengde")
plt.ylabel("Akselerasjon")
"""




"""
x = np.linspace(0,2,21)
y1 = x
y2 = x**2
y3 = np.sqrt(x)
y4 = x**3

plt.figure("fig1")
plt.plot(x,y1, ".-r")

plt.figure("fig2")
plt.plot(x,y2, ".-g")


plt.figure("fig3")
plt.plot(x,y4, ".-y")

plt.figure("fig1")
plt.plot(x, y3, ".-b")
"""
"""
plt.subplot(2,2,1)
plt.plot(x,y1, "*--b")
plt.title("x")

plt.subplot(2,2,2)
plt.plot(x,y2, "*--g")
plt.title("x^2")

plt.subplot(2,2,3)
plt.plot(x,y3, "*--y")
plt.title("Kvadratrot")

plt.subplot(2,2,4)
plt.plot(x,y4, "*--r")
plt.title("x^3")
"""