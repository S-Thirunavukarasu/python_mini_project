import random

def guess_number():
    while True:
        user_choice=int(input("Enter a number from 1 to 10 : "))
        comp_choice=random.randint(1,10)
        if user_choice==comp_choice:
            print(f"You Won!.You and computer have chosen {comp_choice}")
            break
        else:
            print(f"You choose {user_choice} but computer choose {comp_choice}")
            continue
guess_number()