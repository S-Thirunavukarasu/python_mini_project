import random

def r_p_s():
    lst=["r","p","s"]
    while True:
        user_choice=input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice not in lst:
            print("Invalid choice!")
            continue

        comp_choice=random.choice(lst)

        if user_choice==comp_choice:
            print ("That's tie")

        elif(
        (user_choice=="r" and comp_choice=="s") or 
        (user_choice=="p" and comp_choice=="s") or 
        (user_choice=="s" and comp_choice=="p")):
            print( "You Won!")

        else:
            print ("Computer Won!")

        start_again=input("Continue? (y/n)").lower()
        if start_again=="y":
            continue
        elif start_again=="n":
            break
    
r_p_s()