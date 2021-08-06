# #1-usul.
# def sign(x):        #bu sign degan funksiya . hech x parametrga ega 
# 	if x>0:
# 		print(1)    #bu x ni tekshirib ekranga qiymatini chiqarib beradi
# 	elif x<0:
# 		print(-1)
# 	else:
# 		print(0)

# sign(-3)

#qiymat qaytaruvchi funksiya yaratamiz
def sign(x):
	if x>0:
		return 1
	elif x<0:
		return -1
	else:
		return 0
y=sign(8)
print(y)
