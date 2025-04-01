import random

lst=["r","p","s"]

def get_user_choice():
    while True:
        user_choice=input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice not in lst:
            print("Invalid choice!")
            continue
        return user_choice
    
def winner_selection(user_choice,comp_choice):
    if user_choice==comp_choice:
        print ("That's tie")
    elif(
        (user_choice=="r" and comp_choice=="s") or 
        (user_choice=="p" and comp_choice=="s") or 
        (user_choice=="s" and comp_choice=="p")):
        print( "You Won!")
    else:
        print ("Computer Won!")

def r_p_s():
    while True:
        #printing user_choice from get_user_choice() line 5
        user_choice=get_user_choice()
        #printing computer choice from lst decalred globally at line 3
        comp_choice=random.choice(lst)
        #selection the winner function at line 13
        winner_selection(user_choice,comp_choice)    
        #Start playing again from start
        start_again=input("Continue? (y/n)").lower()
        if start_again=="y":
            continue
        elif start_again=="n":
            break
    
r_p_s()