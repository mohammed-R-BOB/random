import random
user_answer = input("enter password of 4-digit: ")
if len(user_answer) != 4:
    print("password must be 4-digit")
    exit()
else:
    computer_answer = random.randint(1000, 9999)
print("computer answer is: ", computer_answer)
if int(user_answer) == int(computer_answer):
    print("you gussed right!!")
    print("your answer is: ", user_answer)
    print("computer answer is: ", computer_answer)
else:
    print("you gussed wrong!!")
    print("your answer is: ", user_answer)
    print("computer answer is: ", computer_answer)
    print("try again")
