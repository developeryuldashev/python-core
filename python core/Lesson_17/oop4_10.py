# coding=utf-8
from Stack import Stack
from Labirint import Labirint
a = [[1,0,0,0],
     [1,1,1,0],
     [0,0,1,1],
     [1,1,1,0],
     [0,1,0,1],
     [1,1,1,1]]
labr = Stack(a)
labr.print()
game = Labirint(labr,0,0,3,5)
for i in range(500):
    x = game.gaming()
    if x[0]<20:
        print(x)
