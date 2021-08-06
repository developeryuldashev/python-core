n=256
sanoq=0
while n>2:
    n/=2
    sanoq+=1
if n==2:
    print(f"bu 2 ning {sanoq+1} darajasi")
else:
    print('bu ikkining darajasi emas')