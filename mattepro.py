import cmath
import numpy
import math
from sympy import Symbol, Derivative
import scipy
import scipy.misc

iterations = 100
x = 0
y = 1
z = 1
t = 1
u = 1
v = 1

# First calculations, to make it easier to initialize loop
newton_result = math.sin(math.radians(1))/math.cos(math.radians(1))
newton_result2 = math.sin(math.radians(y))/(math.cos(math.radians(y)) - 1)
newton_result3 = math.sin(math.radians(z)-z**5)/(math.cos(math.radians(z)) - 5*z**4)
newton_result4 = math.sin(math.radians(t) * t**4)/(t**3 * (4 * math.sin(math.radians(t)) + t * math.cos(math.radians(t))))
newton_result5 = (u**4 - 16)/(4*u**3)
newton_result6 = (v**10-1)/(10*v**9)

print(newton_result2)

while newton_result != 0:
    newton_result = math.sin(math.radians(newton_result))/math.cos(math.radians(newton_result))
    x += 1
    print("Iterasjon", x, "gir resultat: ", newton_result)
    if(newton_result == 0):
        print("Fant nullpunkt")
        break

# No point in going above 360, that's one whole circle. Dividing by 360 also gives divide by 0 error
# You can  expand the loop to run forever if you change the while condition and the if-statement will catch
# the divide by 0 error and continue on.

while y < 360:
    if((math.cos(math.radians(y)) - 1) == 0):
        y +=1
    newton_result2 = math.sin(math.radians(y))/(math.cos(math.radians(y)) - 1)
    print(newton_result2)
    print("Iterasjon", y, "gir resultat: ", newton_result2)
    if(newton_result2 == 0):
        print("Fant nullpunkt")
        break
    y += 1

for x in range(iterations):
    newton_result3 = math.sin(math.radians(z)-z**5)/(math.cos(math.radians(z)) - 5*z**4)
    print("Iterasjon", x, "gir resultat: ", newton_result3)
    if(newton_result3 == 0):
        print("Fant nullpunkt")
        break
    z += 1

for x in range(iterations):
    newton_result4 = math.sin(math.radians(t) * t**4)/(t**3 * (4 * math.sin(math.radians(t)) + t * math.cos(math.radians(t))))
    print("Iterasjon", x, "gir resultat: ", newton_result4)
    if(newton_result4 == 0):
        print("Fant nullpunkt")
        break
    t += 1

for x in range(iterations):
    newton_result5 = (u**4 - 16)/(4*u**3)
    print("Iterasjon", x, "gir resultat: ", newton_result5)
    if(newton_result5 == 0):
        print("Fant nullpunkt")
        break
    u += 1

for x in range(iterations):
    newton_result6 = (v**10-1)/(10*v**9)
    print("Iterasjon", x, "gir resultat: ", newton_result5)
    if(newton_result6 == 0):
        print("Fant nullpunkt")
        break
    v += 1

