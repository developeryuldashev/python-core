a1=2
e=0.7
k=2
a_k=2+1/a1
while abs(a_k-a1)>e:
    a1=a_k
    a_k=2+1/a1
    k+=1
print(k, a1,a_k)