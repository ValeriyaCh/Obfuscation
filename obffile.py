
from sympy import *

def wtf(a, b,c,
        d,e):
    n = c*d
    m = a * b


    g = e + n + m
    while a != 0 and b != 0:
        if a > b:
            a %=\
                b
            h = 4 * \
                65
        else:
            h = b + c
            b %=a##go away
            h = 4*65

    return g + m // (a + b) - e - c * d - m + h

I=1.8
for i in range (20):
    if i>0:
        I = I+(((cos(i*0.05) - 1 + ((i*
                                     0.05)**2)/2)/(i*0.05)**(1/2)) +
               ((cos((i+1)*
                     0.05) - 1 + (((i+1)*0.05)**2)/2)/
                ((i+1)*0.05)**(1/2)))/\
            2*0.05
    else:
        I = I + (0 + (
                    (cos((i + 1) * 0.05) - 1 +
                     ((i + 1) * 0.05) ** 2 / 2) / ((i + 1) * 0.05) **
                    (0.5))) / 2 * 0.05
x = int(input('go='))
y = int(input('away='))
c = x + \
    y
d = x -\
    y
e = wtf(x,y,c,
        d,0)

print('Realy:', e-260)
