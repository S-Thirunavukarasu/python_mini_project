# Creation of dictionary 
contacts=dict()
# 1. Add contact
def add_contact():
    name=input("Enter name : ")
    number=input("Enter number : ")
    if name in contacts:
        print(f"{name} already exists with number {contacts[name]}")
        update_input=input("Do you want to overwrite the contact (y/n) : ").lower()
        if update_input!="y":
            print("Contact not updated.")
            return
    contacts[name]=number
    print(f"{name} has been successfully added!")
# 2. View contacts
def view_contact():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact list : ")
        for contact in contacts:
            print(f"{contact} : {contacts[contact]}")
# 3. Search contact
def search_contact(name_to_search):
    if name_to_search not in contacts:
        print("Contact not found!")
    else:
        print(f"Name : {name_to_search} | Number : {contacts[name_to_search]}")
# 4. Delete contact
def delete_contact():
    if not contacts:
        print("Contact list is empty!")
        return
    else:
        delete_contact_input=input("Enter name to delete : ")
        if delete_contact_input not in contacts:
            print("Contact not found!")
        else:
            del contacts[delete_contact_input]
            print(f"Contact {delete_contact_input} has been successfully removed.") 

def main():
    print("Welcome to Contact Book!")
    while True:
        print("1. Add contact\n2. View contact\n3. Search contact\n4. Delete contact\n5. Exit")
        try:
            user_choice=int(input("Enter a number (1,2,3,4,5) : "))
        except ValueError:
            print("Invalid choice")
            continue
        if user_choice==1:
            add_contact()
            continue
        elif user_choice==2:
            view_contact()
            continue
        elif user_choice==3:
            name_to_search=input("Enter name to search : ")
            search_contact(name_to_search)
            continue
        elif user_choice==4:
            delete_contact()
            continue
        elif user_choice==5:
            break
        else:
            print("Invalid choice")
            continue
main()
