a=[2,3,7,4,9,1,6,5]
b=[8,1,23,9,20,1,3,6]
i=0
b=[]
while i<len(a):
    h=a[i]
    if h in b:
        b.append(h)
    if h in a:
        b.append(h)
    i=i+1
print(a)        