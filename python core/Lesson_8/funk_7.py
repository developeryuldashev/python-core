def Quarter(x,y):
	if x>0 and y>0:
		return 1
	elif x>0 and y<0:
		return 4
	elif x<0 and y>0:
		return 3
	elif x<0 and y<0:
		return 3
	elif x==0 and y==0:
		return 'kordinata boshida'
	elif x==0 and y!=0:
		return 'y o\'qida'
	else:
		return 'x o\'qida'
kor1=Quarter(2,3)
kor2=Quarter((-2),3)
kor3=Quarter(2,-3)
kor4=Quarter(0,0)
print(kor1)
print(kor2)
print(kor3)
print(kor4)
print(Quarter(0,2))
print(Quarter(2,0))