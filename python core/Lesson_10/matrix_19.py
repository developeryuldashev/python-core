a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for i in a:
    s=0
    p=1
    for j in i:
        s+=j
        p*=j
    print(f"{a.index(i)} satr yig'indisi:=",s)
    print(f"{a.index(i)} satr ko'paytmasi :=",p)
