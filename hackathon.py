s=input("enter the string")
c=input("enter the char to check the frequency")
count=0
for i in s:
    if i==c:
        count=count+1
print(c,"words",count,"time(s)")   
