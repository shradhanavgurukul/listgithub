n = [19, 17, 12, 17, 17, 18, 10, 17,12,14, 19, 17, 12, 13, 11]
i=0
a=[]
while i<len(n):
    h=n[i]
    if h not in a:
        a.append(h)
    i=i+1
print(a)


