# coding=utf-8      2,5,3,1,4,9,5
a = [2,5,3,1,4,9,5]

for i in range(1,len(a)-1):
    if a[0]<a[i]<a[len(a)-1]:
        print(i+1)
        ind = i+1
print(ind)