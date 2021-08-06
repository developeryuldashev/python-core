import csv
""" bu csv faylga lug'at yozish"""
faylnomi='users1.csv'
# users1=[
#     {'ism':'dilshod', 'yosh':21},
#     {'ism':"to'ychi", 'yosh':24},
#     {'ism':'islom', 'yosh':22}
# ]
# with open(faylnomi,'w',newline='') as fayl:
#     ustunlar=['ism','yosh']
#     writer=csv.DictWriter(fayl,fieldnames=ustunlar)
#     writer.writeheader()
#     # bir nechta qtorlarni yozish uchun
#     writer.writerows(users1)
#     user={'ism':'shaxnoza','yosh':18}
#     writer.writerow(user)

""" yozilgan ma'lumotlarni o'qib olamiz"""
with open(faylnomi,'r',newline='') as fayl:
    reader=csv.DictReader(fayl)
    for row in reader:
        print(row['ism']+'--'+row['yosh'])

