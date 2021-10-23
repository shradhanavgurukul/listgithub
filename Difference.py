a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
j=[]
i=0
while i<len(a):
    k=a[i]
    if k in b:
        j.append(k)
    i=i+1
print(j)       


# year=int(input("enter the year"))
# i=0
# while i<year:
#     if i%4==0 or i%400:
#         print("it is a leap year")
#     elif i%100:
#         print("it is satishfied")
#     else:
#         print("it is not leap year")
#     i=i+1



