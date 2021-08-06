a=-1
b=2
c=-1
# if a>0 and b>0 and c<0 or a<0 and b<0 and c>0:
#     t=3
# elif a>0 and b<0 and c>0 or a<0 and b>0 and c<0:
#     t=2
# elif a>0 and b<0 and c<0 or a<0 and b>0 and  c>0:
#     t=1
# else:
#     t='hammasining ishirasi bir xil'
# print(t)
a1,b1,c1=a/abs(a),b/abs(b),c/abs(c)
if a1!=b1 and b1==c1:
    print(1)
if a1==b1 and b1!=c1:
    print(3)
if a1!=b1 and a1==c1:
    print(2) 
