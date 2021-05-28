import random
list = ["snake","water","gun"]
count=10
user_score = 0
computer_score = 0
while(count!=0):
    user = input("choose anyone from list:\n")
    print("computer selected:")
    comp = random.choice(list)
    print(comp)
    if(user==comp):
        print("tie")
        count=count-1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left",count)
    elif(user=="snake" and comp=="water"):
        print("user won!")
        count = count - 1
        user_score = user_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left",count)
    elif(user=="snake" and comp=="gun"):
        print("computer won!")
        count = count - 1
        computer_score = computer_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left",count)
    elif(user=="water" and comp=="snake"):
        print("computer won!")
        count = count - 1
        computer_score = computer_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left", count)
    elif(user=="water" and comp=="gun"):
        print("user won!")
        count = count - 1
        user_score = user_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left", count)
    elif(user=="gun" and comp=="snake"):
        print("user won!")
        count = count - 1
        user_score = user_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left", count)
    elif(user=="gun" and comp=="water"):
        print("computer won")
        count = count - 1
        computer_score = computer_score + 1
        print(f"user score:{user_score} and computer score:{computer_score}")
        print("no. of matches left", count)
    else:
        print("wrong input")
        print("no. of matches left", count)

if(user_score > computer_score):
    print(f"user won by {user_score - computer_score} points")
elif(user_score < computer_score):
    print(f"computer won by {computer_score - user_score} points")
else:
    print("result id tie")

