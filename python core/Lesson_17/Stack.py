# coding=utf-8
# coding=utf-8
class Stack:
    def __init__(self,labirint):
        self.lbr = labirint
    def toTop(self,x,y):
        if y-1>=0:
            return self.lbr[y-1][x] == 1
        else:
            return False
    def toDown(self,x,y):
        if y+1<len(self.lbr):
            return self.lbr[y+1][x]==1
        else:
            return False
    def toRight(self,x,y):
        if x+1<len(self.lbr[0]):
            return self.lbr[y][x+1] == 1
        else:
            return False
    def toLeft(self,x,y):
        if x-1>=0:
            return self.lbr[y][x-1] == 1
        else:
            return False

    def print(self):
        for i in self.lbr:
            for j in i:
                print(j,end='   ')
            print()