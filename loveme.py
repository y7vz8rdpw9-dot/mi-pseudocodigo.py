import math 
from turtle import *

def hearta(G):
    return 15 * math.sin(G)**3
def heartb(G):
    return 12 *math.cos(G)-5*\
    math.cos(2*G)-2*\
    math.cos(3*G)-\
    math.cos(4*G)
speed(9000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        color("red")
        goto(0,0)
done()

    