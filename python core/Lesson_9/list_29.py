a=[1,1,6,5,3,4,5]
t=a[1]
for i in range(1,len(a),2):
    if t<a[i]:
        t=a[i]
print(t)