# k=3
# x=int(input('kiritng x='))
# print(x)
# while x!=0:
# 	x=int(input('kiriting x='))
# 	if x>k:
# 		y=x
# 	break;
# print(y)


# k=8
# x=int(input('kirit:'))
# xmax=''
# r=False
# while x!=0:
# 	if (not r)and x>k:
# 		xmax=x
# 	r=r or x>k
# 	x=int(input('kirit:'))
# print(xmax)

k=3
x=int(input('x='))
xmax=''
r=False
while x!=0:
	if (not r) and x>k:
		xmax=x
	r=r or x>k
	x=int(input('x='))
print(xmax)