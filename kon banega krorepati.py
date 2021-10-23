print("welcome to kbc")
print("kon banega krorpati")
question_list = ["1).How many continents are there?",  

                "2).What is the capital of India?", 

				"3).NG mei kaun se course padhaya jaata hai?"]


options_list = [["1.four","2.nine","3.seven","4.eight"],

               ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],

               ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]

solution = [3, 4,1]

answer=["3.seven","4.eight","3.chennai","4.delhi" "1.software engineering","2.counseling"]
i=0
amount = 1000
count = 0
b=0
a=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<=len(options_list[i]):
        print(options_list[i][j])
        j=j+1
        lifeline=input("do you want lifeline")
        if lifeline=="yes":
            print("5050")
            if count==5050:
                print(answer[b+i])
                print(answer[b+a])
                num=int(input("enter the answer"))
                if num==solution[i]:
                    print("your answer is right")
                    print("you won",amount,"$")
                else:
                    print("answer is wrong")
                    print("you loose the game")
                    break
                count=count+1
                print()
            else:
                print("you had already used lifeline")
                e=int(input("enter the answer"))
                if e==solution[i]:
                    print("your answer is right")
                    print("you won",amount,"$")
                else:
                    print("answer is wrong")
                    print("you loose the game")
                    break
                count=count+1
                print()
    else:
        f=int(input("enter the answer"))
        if f == solution[i]:
            print("your answer is right")
            print("you won",amount,"$")
        else:
            print("answer is wrong")
            print("you loose the game")
            break
        print()
    amount=amount+1000
    i=i+1
    a=a+1
    b=b+1    





                        







                    

















