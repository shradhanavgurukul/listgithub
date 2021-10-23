a=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
i=0
b=[]
while i<len(a):
    k=(a[i])
    b.append(k)
    i=i+1
a.remove(5)
a.remove(3)
a.remove(5)
print(a)

