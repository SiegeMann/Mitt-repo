from sympy import symbols, solve
from sympy import *
print(" ")
print("Dette programmet løser andregradslikningen ax^2 + bx + c = 0.")
x = symbols('x')
a = symbols('a')
b = symbols('b')
c = symbols('c')
x = int
a = float(input("skriv inn konstanten a: "))
b = float(input("skriv inn konstanten b: "))
c = float(input("skriv inn konstanten c: "))
d = b**2-4*a*c
if d > 0:
    print(" ")
    svar1 = (-b- sqrt(b**2 - 4*(a*c)))/(2*a)
    print(" ")
    svar2 = (-b + sqrt(b**2 - 4*(a*c)))/(2*a)
    print("x1 =", N(svar1,1))
    print("x2 =", N(svar2,1))
elif d == 0:
    print(" ")
    print("bare en løsning")
    print(" ")
    svar1 = -b/(2*a)
    print("x =", svar1)
else:
    print("ingen løsning")

    


    
