# print yordamida file ga yozish
# with open ('hello.txt','a') as hello_file:
#     print("xush kelibsiz!", file=hello_file)

# with open('hello.txt','r') as hello_fayl:
    # for satr in hello_fayl:
    #     print(satr, end=' ')
    # satr1=hello_fayl.readline()
    # print(satr1,end=' ')
    # satr=hello_fayl.readline()
    # while satr:
    #     print(satr, end=' ')
    #     satr=hello_fayl.readline()
# with open('hello.txt', encoding="utf8") as hello_fayl:
#     mazmun=hello_fayl.read()
#     print(mazmun)

# file larga ro'yxat yozish

filename='habarlar.txt'
xabarlar=list()
for i in range(4):
    xabar=input("Satrni kiriting "+str(i+1)+":")
    xabarlar.append(xabar+'\n')
print(xabarlar)

# ro'yxatni filega yozish
with open(filename,'w') as fayl:
    for xabar in xabarlar:
        fayl.write(xabar)
# faylni o'qish
with open(filename,'r') as fayl1:
    for satr in fayl1:
        print(satr,end=' ')

