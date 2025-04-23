# Convert Kilometers to Miles
def kilometer_to_miles():
    try:
        kilometer=int(input("Enter kilometer : "))
    except:
        print("Invalid input")
        return
    miles = kilometer * 0.621371
    print(f"{kilometer}kilometer = {miles:.2f}miles")
# Convert Celsius to Fahrenheit
def celsius_to_farenheit():
    try:
        celsius=int(input("Enter celcius : "))
    except:
        print("Invalid input")
        return
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}celcius = {fahrenheit:.2f}fahrenheit")
# Convert Kilograms to Pounds
def kilograms_to_pounds():
    try:
        kilogram=int(input("Enter kilogram : "))
    except:
        print("Invalid input")
        return
    pounds = kilogram * 2.20462
    print(f"{kilogram}kilogram = {pounds:.2f}pounds")
# Convert Miles to Kilometers
def miles_to_kilometer():
    try:
        mile=int(input("Enter mile : "))
    except:
        print("Invalid input")
        return
    kilometer = mile * 1.60934
    print(f"{mile}mile = {kilometer:.2f}kilometer")

# main
def main():
    while True:
        print("Unit Converter (CLI Version)")
        print("1. Km to Miles\n2. Celsius to Fahrenheit\n3. Kg to Pounds\n4. Miles to Km\n5. Exit")
        try:
            choice_selection=int(input("Enter choice(1,2,3,4,5) : "))
        except:
            print("Invalid choice")
            continue
        if choice_selection==1:
            kilometer_to_miles()
            continue
        elif choice_selection==2:
            celsius_to_farenheit()
            continue
        elif choice_selection==3:
            kilograms_to_pounds()
            continue
        elif choice_selection==4:
            miles_to_kilometer()
            continue
        elif choice_selection==5:
            break
        else:
            print("Invalid choice")
            continue
main()