current_year=int(input("enter the current year"))
birth_year=int(input("enter the birth year"))
if current_year-birth_year>=0:
    age=birth_year-current_year
    print("this year age",age)
elif current_year-birth_year<=1:
    age1=birth_year-current_year
    print("this year age",age1) 
else:
    print("this is not year age")     


