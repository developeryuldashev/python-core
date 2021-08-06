def Calc(a,b,op):
	if op==1:
		return a-b
	elif op==2:
		return a*b
	elif op==3:
		return a/b
	else:
		return a+b
op1=Calc(6,3,1)
op2=Calc(6,3,2)
op3=Calc(6,3,3)
op4=Calc(6,3,4)
op5=Calc(6,3,5)
print(op1,op2,op3,op4,op5)
print(Calc(b=3,a=6,op=0))