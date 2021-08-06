a=[16,5,3,4,5]
t=a[0]
for i in range(0,len(a),2):
    if t>a[i]:
        t=a[i]
print(t)

