import csv
filename='users.csv'
# users=[
#     ['Ali',25],
#     ['vali',24],
#     ['dilnoza',18]
# ]
# with open(filename,'w',newline='') as fayl:
#     yozamiz=csv.writer(fayl)
#     yozamiz.writerows(users)
# with open(filename,'a',newline='') as fayl:
#
#     user=['shaxnoza',19,'dilshod']
#     yozamiz=csv.writer(fayl)
#     yozamiz.writerow(user)
with open(filename,'r',newline='') as fayl:
    uqiymiz=csv.reader(fayl)
    for row in uqiymiz:
        print(row[0].title()+'--'+row[1])