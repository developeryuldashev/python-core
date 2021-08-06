# def isPowerS(k):
# 	while k>1:
# 		k/=5
# 	r=(k==1)
# 	return r
# 	"""bu kiritilgan sonning 5 ning 
# 	darajasimi yo'qmi aniqlaydigan funksiya"""
# l=isPowerS(6251)
# print(l)
# t=0
# n=10
# while n>0:
# 	x=int(input('x='))
# 	if isPowerS(x):
# 		t=t+1
# 	n-=1
# print(t)


def isPowerS(a):
	while a>=5:
		a=a/5
	if a==1:
		return True
	else:
		return False

sanoq=0
for i in range(1,11):
	if isPowerS(i):
		sanoq+=1
print(sanoq)
