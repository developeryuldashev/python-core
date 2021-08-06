# coding=utf-8
a = [7,9,3,1,5,8]
k,l = 3,4
s = 0
for i in range(k-1,l):
    s += a[i]
print(s/(l-k+1))