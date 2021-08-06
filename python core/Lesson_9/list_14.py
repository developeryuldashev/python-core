a=[5,4,3,2,1,0]
juft_in=[]
toq_in=[]
i=0
n=len(a)
while n-1>i:
    toq_in.append(a[i])
    juft_in.append(a[i+1])
    i+=2
print(toq_in)
print(juft_in)

