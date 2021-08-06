n=156239
t=0
k=0
summ=0
while n>=1:
    t=n%10
    n=n//10
    k+=1
    summ+=t
print(summ, k)