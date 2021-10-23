mainStr="the quick brown fox jumped over the lazy dog.the dog slept over the verandah"
subStr=mainStr.split()
i=0
while i<len(subStr):
    if subStr[i]=="over":
        # i=i+1
        print(subStr[i],end=" ")
    i=i+1    


k=int(input("enter the number"))
i=0
while i<=10:
    print(i,i*k)
    i=i+1