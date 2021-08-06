# coding=utf-8
a = [5,1,2,4,3,7,1,1,1,5,5,5]

b = []

for i in a:
    if not i in b:
        b.append(i)
print(len(b))