
def simple_intrest(principle,years,rate):
    si=round((principle*years*rate)/100)
    amount=round(principle+si)
    print(f"Simple intrest = {si}")
    print(f"Total amount = {amount}")

def compound_intrest(principle,years,rate):
    amount=round(principle*(1+rate/100)**years)
    ci=round(amount-principle)
    print(f"Compound intrest = {ci}")
    print(f"Total amount = {amount}")

def main():
    
    while True:
        print("*******************")
        print("1.SIMPLE INTREST\n2.COMPOUND INTREST")
        print("*******************")
        choice=input("Enter '1' for simple intrest or '2' for comopound intrest : ")
        principle=int(input("Enter principle : "))
        years=int(input("Enter number of years : "))
        rate=int(input("Enter rate of intrest : "))
        if choice=='1':
            simple_intrest(principle,years,rate)
            break
        elif choice=='2':
            compound_intrest(principle,years,rate)
            break
        else:
            print("Invalid choice! Select either '1' or '2'")
main()

