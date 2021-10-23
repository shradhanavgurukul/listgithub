magic_square=[
        [8,3,4],
        [1,5,9],
        [6,7,2]
]              
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+magic_square[i][j]
        j=j+1
    i=i+1
print(sum)
r=0
while r<len(magic_square):
    k=0
    sum1=0
    while k<len(magic_square):
        sum1=sum1+magic_square[r][k]
        k=k+1
    r=r+1
print(sum1)    


















 