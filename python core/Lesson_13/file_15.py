with open('seriyalisonlar.txt','r') as file:
    a=file.readlines()
for b in a:
    for i in b:
        print(i,end='\t')
    print('-----')
