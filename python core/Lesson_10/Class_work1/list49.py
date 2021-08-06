# coding=utf-8
a = [5,9,2,7,1,3,6,4]
b = a.copy()
t = []
b.sort()
r = True
for i in range(len(a)):
    r = r and i+1 == b[i]
    t.append(i+1)
if r:
    print(0)
else:
    for i in range(len(a)):
        if not a[i] in t:
            print(i+1)

# 1,3,2,4,5,7,6
# 1,2,3,4,5,6,7