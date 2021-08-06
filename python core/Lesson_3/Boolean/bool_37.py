x1,y1,x2,y2=1,4,2,5
r=(abs(x2-x1)==abs(y2-y1)==1) or (x1==x2 and abs(y2-y1)==1) or (y1==y2 and abs(x2-x1)==1)
print(r)