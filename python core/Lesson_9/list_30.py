a=[1,6,5,3,4,5]
sanoq=0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        print(i)
        sanoq+=1
print("o'ng tomondagi elementdan katta elentlar soni=:",sanoq)

