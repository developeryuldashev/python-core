a=[1,2,3,4,5,6,7,8,9,10,11,12]
while len(a)>0:
    if len(a)>4:
        print(a[0],a[1],a[len(a)-1],a[len(a)-2], end=' ')
        a.remove(a[0])
        a.remove(a[0])
        a.remove(a[len(a)-1])
        a.remove(a[len(a)-1])
    else:
        print(a[0],end=' ')
        a.remove(a[0])