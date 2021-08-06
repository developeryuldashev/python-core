def sonlar(n):
    f=open('sonlar.txt','w')
    for i in range(1,n+1):
        f.write(str(i)+'\t')
    f.close()
n=105
d=sonlar(n)
f = open('sonlar.txt','r')
a = f.read()
b = list(a.split())
f.close()
print(b[10])
with open('toq_urindagilar.txt','w') as file1, open('juft_urindadilar.txt','w') as file2:
    for i in range(0,n-1,2):
        file1.write(str(b[i]+'\n'))
        file2.write(str(b[i+1]+'\t'))








