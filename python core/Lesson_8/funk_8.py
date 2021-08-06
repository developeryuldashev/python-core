def Ever(k):
	if k%2==0:
		r=True
		return r
	else:
		r=False
		return r
#print(Ever(8))
t=0    #juft sonlarni sanash uchun
n=10    # tekshirilishi kerak bo'lgan sonlar miqdori
n1=n
while n>0:
	x=int(input('x='))
	if Ever(x):
		t+=1
	n-=1
print(f"{t} ta si just {n1-t} tasi toq")