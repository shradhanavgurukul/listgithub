list=[1,1,2,2,3,4,5,5,5,6,7]
a=[]
for i in list:
    m=[]
    if i not in a:
        a.append(i)
        m.append(list)
print(m)
i=0
while i<len(a):
    count=0
    for j in range(0,len(list)):
        if a[i]==list[i]:
            count=count+1
    print([a[i],count]) 
    i=i+1




    


       