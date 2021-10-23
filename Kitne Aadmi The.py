elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even_number=0
odd_number=0
s=[]
p=[]
length=len(elements)
while i<len(elements):
    if elements[i]%2==0:
        s.append(elements[i])
        even_number=even_number+1
    else:
        p.append(elements[i])
        odd_number=odd_number+1
    i=i+1
print("even number","=",even_number,s)
print("odd number","=",odd_number,p)  