numbers=[50,40,23,70,56,12,5,10,7]
i=1   
a=[]
b=[] 
while i<len(numbers):
    j=numbers[i]
    if j>20:
        a.append(j)     
    else:
        b.append(j)
    i=i+1
print("20 se bada hai",a)     
print("40 se chota hai",b)          
