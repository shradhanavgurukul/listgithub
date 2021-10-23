number=30
n=[10,11,12,13,14,17,18,19]
i=0
b=[]
while i<len(n):
    if n[i]+n[-i]==number:
        k=(n[i],n[-i])
        b.append(k)
    i=i+1
print(b)        