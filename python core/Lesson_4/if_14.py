a,b,c=4,2,6
if a>b and b>c:
    max1=a
    min1=c
elif c>b and b>a:
    max1=c
    min1=a
elif a>c and c>b:
    max1=a
    min1=b
elif b>c and c>a:
    max1=b
    min1=a
elif b>a and a>c:
    max1=b
    min1=3
else:
    max1=c
    min1=b
print(f"eng kattasi {max1} , eng kichigi {min1}")

