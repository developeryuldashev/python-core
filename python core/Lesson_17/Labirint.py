# coding=utf-8
from random import choice
class Labirint:
    def __init__(self,l,inX,inY,outX,outY):
        self.labr = l
        self.inX = inX
        self.inY = inY
        self.outX = outX
        self.outY = outY

    def findPath(self,x,y):
        paths = []
        if self.labr.toTop(x,y):
            paths.append((x,y-1))
        if self.labr.toDown(x,y):
            paths.append((x,y+1))
        if self.labr.toRight(x,y):
            paths.append((x+1,y))
        if self.labr.toLeft(x,y):
            paths.append((x-1,y))
        return paths
    def gaming(self):
        c = 0
        cc = []
        x,y = self.inX,self.inY
        while not (x == self.outX and y == self.outY):
            paths = self.findPath(x,y)
            x,y = choice(paths)
            cc.append((x,y))
            c += 1
        return c,cc