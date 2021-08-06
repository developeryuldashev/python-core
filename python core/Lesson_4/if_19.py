a,b,c,d=9,3,5,2
if a%2==b%2==c%2!=d%2:
    t=4
elif a%2==b%2==d%2!=c%2:
    t=3
elif a%2==c%2==d%2!=b%2:
    t=2
elif b%2==c%2==d%2!=a%1:
    t=1
else:
    t='bu yerda uchtasi hech bir 3 tasi juft toqligi bilan boshqasidan farq qilmaydi'
print(t)