numbers= [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=numbers[0]
while i<len(numbers):
    if numbers[i]<a:
       a=numbers[i]
    i=i+1
numbers.remove(a)
i=0
b=numbers[0]
while i<len(numbers):
    if numbers[i]<b:
        b=numbers[i]
    i=i+1
print(b)             