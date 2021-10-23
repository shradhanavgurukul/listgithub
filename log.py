list=[-2,3,4,-1,-3]
i=0
a=[]
while i<len(list):
    k=list[i]
    if k<0:
        a.append(0)
    elif k>0:
        a.append(i)
    i=i+1
print(a,i)



b=[]
for i in list:
    if i<0:
        b.append(0)
    elif i>0:
        b.append(i)
    i=i+1
print(b)
