#19-masala
a=[1,3,5,2,1.5,4]  #agar 1 chi index kk bo'lsa

ind=None
for i in range(1,len(a)-1):
    if a[0]<a[i]<a[len(a)-1]:
        ind=i
        break
print(ind)

# for orqali
# a=[1,3,5,2,1.5,4]

# ind=None
# for i in range(1,len(a)-1):
#     if a[0]<a[i]<a[len(a)-1]:
#         ind=i
# print(ind)



#n=len(a)
# i=1
# shart1='bu shart bajarilmadi' #None
# while n-1>i:
#     if a[0]<a[i]<a[n-1]:
#         shart1=i
#     i+=1
# print(shart1)



