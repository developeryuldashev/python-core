s=0
with open('son_yoz.txt','r') as file:
    reader=file.read()
    a=list(reader.split())
    for i in range(len(a)):
        s+=int(a[i])
print(s/len(a))
