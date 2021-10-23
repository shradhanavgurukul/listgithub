elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42,43]
i=0
a=[]
b=[]
avg1=0
avg2=0
total_avg=0
while i<len(elements):
    total_avg+=elements[i]
    total_avg+total_avg/len(elements)
    total_avg=total_avg/11
    j=elements[i]
    if j%2==0:
        a.append(j)
        avg1=avg1+j
        avg1=avg1/4
    else:
        b.append(j)
        avg2=avg2+j
        avg2=avg2/7
    i=i+1
print("the average of even number",a,avg1)
print("the average of odd number",b,avg2)


