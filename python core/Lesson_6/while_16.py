k=10
p=40
s=k
c=1
while s<40:
    c+=1
    k*=(1+p/100)
    print(k)
    s+=k
print(f"{c} kunda jami {s} km")