# a=[ 'n', 'i  ', 't', 'i', 'n' ]
# b=[]
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# print(b)
# if b==a:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")  


a=[[2,4,6],[2,5,3]]
i=1
b=[]
while i<len(a):
    if i%2:
        b.append(a[i])
        print(b)
        k=0
        while k<len(a):
            if i%3:
                b.append(a[k])
                print(b)
            k=k+1
    i=i+1
        
 
    





