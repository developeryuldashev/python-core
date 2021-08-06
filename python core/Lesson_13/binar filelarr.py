import pickle
filename='user.dat'
ism='ali'
yosh=25
# with open(filename,'wb') as fayl:
#     pickle.dump(ism,fayl)
#     pickle.dump(yosh,fayl)
with open(filename,'rb') as file:
    pickle.load(file)
    pickle.load(file)
    print("Ism: ",ism.title(),"\tYosh: ",yosh)