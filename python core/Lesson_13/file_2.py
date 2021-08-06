s='son_yoz.txt'
n=100
with open(s,'w') as number:
    for i in range(0,n+1,2):
        number.writelines(str(i)+'\n')
# readl=open('son_yoz.txt','r')
# print(readl)
# readl.close()

