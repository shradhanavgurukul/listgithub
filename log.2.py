k=[1,2,2,5,4,4,8]
i=0
a=[]
count=0
while i<len(k):
    c=(k[i])
    if c not in a:
        a.append(c)
        count=count+1
    i=i+1
print(a,count)



list=[1,2,3,1,2,2]
i=0
a=[]
while i<len(list):
    k=(list[i])
    if k not in a:
        a.append(k)
    i=i+1
print(a)
