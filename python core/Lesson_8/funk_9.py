# n=16
# i=0
# r=False
# m=n//2
# while m>0:
# 	i+=1
# 	r=r or (i*i==n)	
# 	m-=1
# print(r)


# def isSquare(k):
# 	i=0
# 	r=False
# 	m=(k//2)
# 	while m>0:
# 		i+=1
# 		r=r or (i*i==k)
# 		break
# 		m-=1
# 	return r


# t=0
# n=10
# while n>0:
# 	x=int(input('x='))
# 	if isSquare(x):
# 		t+=1
# 	n-=1
# print(t)

def isSquare(n):
	i=1
	m=n//2
	r=False
	while m>0:
		i=i+1
		r=r or (i*i==n)
		if r:
			break
		m-=1
		#print(r)
	return r
t=0
k=10
while k>0:
	x=int(input('x='))
	if isSquare(x):
		t+=1
	k-=1
print(t)




