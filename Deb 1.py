marks = [10, 32, 42, 65, 67, 89, 76, 38,67,80]
length=len(marks)
counter=0
total_marks=0
while counter<len(marks):
    total_marks=marks[counter]+total_marks
    counter=counter+1
print("total marks"+str(total_marks))  



