# coding=utf-8
a = [3,5,9,6,1]
b = []
for i in a:
    if i<5:
        b.append(2*i)
    else:
        b.append(i/2)
print(b)