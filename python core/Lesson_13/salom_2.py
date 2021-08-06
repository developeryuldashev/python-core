#
# with open('salom.txt','w') as file_obj:
#     file_obj.write('Onajonim mehribonim')
# with open('salom.txt','a') as xasan:
#     xasan.write('\nDadajon men sizni yaxshi ko\'raman')
# with open('salom.txt','r') as file_obj:
#     print(file_obj.read())

# with open('salom.txt','a') as husan:
#     print('Mening eng yaqin dustlarim', file=husan)
#     print(husan.read())

# with open('salom.txt','r') as fayl:
#     for satr in fayl:
#         print(satr, end='')
with open('salom.txt','r') as fayl:
    satr1=fayl.readline()
    print(satr1, end='')
    satr2=fayl.readline()
    print(satr2)


