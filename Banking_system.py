print("*******************")
print("  Banking Program  ")
print("*******************")

balance = 0

def show_balance():
    print(f"Your balance is : {balance}")

def deposit():
    amount=int(input("Enter amount to be deposited : "))
    if amount<0:
        print("Please Enter an amount grater than 0")
    else:
        print(f"Successfully deposited {amount}")
        return amount

def withdraw():
    amount=int(input("Enter amount to withdraw : "))
    if amount<0 or amount>balance:
        print("Invalid transaction")
    else:
        return amount
def main():
    global balance
    while True:
        print("*******************")
        print("1.Show balance\n2.Deposit\n3.Withdraw\n4.Exit")
        print("*******************")
        user_choice=int(input("Enter one choice (1 to 4) : "))
        if user_choice<1 or user_choice>4:
            print("Invalid Choice!! Selcet from 1 to 4")
            continue
        elif user_choice==1:
            show_balance()
            continue
        elif user_choice==2:
            balance +=deposit()
            continue
        elif user_choice==3:
            balance -=withdraw()
            continue
        else:
            print("Thanks! See you soon")
            break
main()