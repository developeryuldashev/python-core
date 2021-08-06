# def RootsCount(a,b,c):
# 	"""kvadrat tenglamani ildizlar sonini 
# 	aniqlovchi funksiya. bu qiymat qaytarmaydi"""
# 	if b**2-4*a*c>0:
# 		print('kv tenglama 2 ta ildizga ega')
# 	elif b**2-4*a*c==0:
# 		print('kv tenglama 1 ta ildizga ega')
# 	else:
# 		print('kv tenglama birorta ildizga ega emas')

# RootsCount(1,-5,6)
# RootsCount(1,-4,4)
# RootsCount(1,4,6)
# print(RootsCount.__doc__)

def Disk(a,b,c):
	D=b*b-4*a*c
	return D

# def RootsCount(a,b,c):
# 	"""bu so'ralgan joyga qiymat qaytaradigan funksiya"""
# 	if b*b-4*a*c>0:
# 		return 2
# 	elif b*b-4*a*c==0:
# 		return 1
# 	else:
# 		return 0
# x,y,z=1,-4,4
# print(RootsCount(x,y,z)) #bu  funksiyani chaqirish
# y=RootsCount(1,3,2)
# print(y)

def RootsCount(a,b,c):
	if Disk(a,b,c)>0:
		return 2
	elif Disk(a,b,c)==0:
		return 1
	else:
		return 0
l=RootsCount(2,-5,6)
print(l)