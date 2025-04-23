expense_dict=dict()
# 1. Add Expense
def add_expense():
    category=input("Enter category : ")
    try:
        amount=int(input("Enter amount : "))
    except ValueError:
        print("Invalid amount")
        return
    if category in expense_dict:
        duplicate_check=input((f"Category {category} alredy exists.\nDo you want to overwrite?(y/n): ")).lower()
        if duplicate_check!="y":
            print("Skipped to update")
        else:
            expense_dict[category]=amount
            print(f"Category {category} of amount {amount} is added!")
    else:
        expense_dict[category]=amount
        print(f"Category {category} of amount {amount} is added!")
# 2. View All Expenses
def view_all_expense():
    if not expense_dict:
        print("No values found!")
        return
    else:
        for key,value in expense_dict.items():
            print(f"Category : {key} | Amount : {value}")
# 3. View Total Spent
def view_total_spent():
    if not expense_dict:
        print("No values found!")
        return
    else:
        total=0
        for i in expense_dict:
            total+=expense_dict[i]
        print(f"Total amount : {total}")
# 4. Search by Category
def search_expense():
    if not expense_dict:
        print("No values found!")
        return
    else:
        name_to_search=input("Enter category to search : ")
        if name_to_search in expense_dict:
            print(f"Category : {name_to_search} | Amount : {expense_dict[name_to_search]}")
        else:
            print("Invalid Category")
            return

# Main
def main():
    while True:
        print("Expense Tracker (CLI Version)")
        print("1. Add Expense\n2. View All Expenses\n3. View Total Spent\n4. Search by Category\n5. Exit")
        try:
            choice_selection=int(input("Enter choice(1,2,3,4,5) : "))
        except ValueError:
            print("Invalid choice!")
            continue
        if choice_selection==1:
            add_expense()
            continue
        elif choice_selection==2:
            view_all_expense()
            continue
        elif choice_selection==3:
            view_total_spent()
            continue
        elif choice_selection==4:
            search_expense()
            continue
        elif choice_selection==5:
            break
        else:
            print("Invalid choice")
            continue
main()
