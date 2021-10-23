evenlist=[2,9,4,7,6,5,8,3,10,1]
# evenlist=int(input("enter the number"))
i=0
while (i<len(evenlist)):
    if (evenlist[i]%2==0):
        evenlist.remove(evenlist[i])
    i=i+1
print("list is removing even numbers=",evenlist)        



a=[1,2,3,4]
i=0
sum=0
avg=0
while i<len(a):
    sum=sum+a[i]
    sum=avg//2
    i=i+1
print(sum,avg)