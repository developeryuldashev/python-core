#6-masala
n=3
p=1
while n>0:
    x=float(input('kiriting x='))
    print(x-int(x))  #sonning kasr qismi sondan butun ayrilganiga teng
    p*=(x-int(x))  #kasr qismlar ko'paytmasi uchun
    n-=1
print(p)