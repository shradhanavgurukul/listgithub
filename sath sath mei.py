elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
a=[]
b=[]
even=0
odd=0
total_count=0
sum1=0
sum2=0
total_sum=0
avg1=0
avg2=0
total_avg=0
while i<len(elements):
    total_sum+=elements[i]
    total_avg+total_sum/len(elements)
    total_count=total_count+1
    total_avg=total_sum/11
    j=elements[i]
    if j%2==0:
        even=even+1
        a.append(j)
        sum1=sum1+j
        avg1=sum1/4
    else:
        odd=odd+1
        b.append(j)
        sum2=sum2+j
        avg2=sum2/7
    i=i+1
print("even number",a,"and sum is","and average is",avg1)
print('odd number',b,"and sum is",sum2,"and averge is",avg2)
print("total sum","=",total_sum)
print("total avg","=",total_avg)
print("total count","=",total_count)
print("count of even number","=",even)
print("count of odd number","=",odd)