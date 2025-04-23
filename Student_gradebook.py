grades_dict=dict()
# Add a student with their marks.
def add_student():
    name=input("Enter name : ")
    try:
        mark=int(input("Enter mark : "))
    except ValueError:
        print("Invalid input")
        return
    grades_dict[name]=mark
    print(f"{name} has been added with mark {mark}!")
# View all students and their marks.
def view_all_student():
    if not grades_dict:
        print("No details found!")
        return
    else:
        for key,value in grades_dict.items():
            print(f"Name : {key} | Mark : {value}")
# Search for a student and view their marks.
def search_student():
    if not grades_dict:
        print("No details found!")
        return
    else:
        name_to_search=input("Enter name to search : ")
        if name_to_search in grades_dict:
            print(f"Marks of {name_to_search} : {grades_dict[name_to_search]}")
        else:
            print("Invalid name")
            return
# Delete a student.
def delete_student():
    if not grades_dict:
        print("No details found!")
        return
    else:
        name_to_delete=input("Enter name to delete : ")
        if name_to_delete in grades_dict:
            del grades_dict[name_to_delete]
            print(f"{grades_dict[name_to_delete]} has been removed!")
        else:
            print("Invalid name")
            return

# Main
def main():
    while True:
        print("Student Gradebook (CLI Version)")
        print("1. Add a student with their marks.\n2. View all students and their marks.\n3. Search for a student and view their marks.\n4. Delete a student.\n5. Exit the app.")
        try:
            choice_selection=int(input("Select the choice(1,2,3,4,5) : "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice_selection==1:
            add_student()
            continue
        elif choice_selection==2:
            view_all_student()
            continue
        elif choice_selection==3:
            search_student()
            continue
        elif choice_selection==4:
            delete_student()
            continue
        elif choice_selection==5:
            break
        else:
            print("Invalid choice")
            continue
main()