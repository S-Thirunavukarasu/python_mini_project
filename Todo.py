task_list=list()
# 1. Add task
def add_task(task_list):
    task_input=str(input("Enter task  : "))
    task_list.append(task_input)
    print(f"{task_input} has been added successfully!")
# 2. View tasks
def view_task(task_list):
    count=1
    if not task_list:
        print("Task list is empty")
    else:
        for i in task_list:
            print(f"{count}. {i}")
            count+=1

# 4. Remove task
def remove_task(task_list):
    if not task_list:
        print("No tasks to remove")
    else:
        task_remove_input=int(input("Enter the number of task you want to remove : "))
        if task_remove_input<1 or task_remove_input>len(task_list):
            print("Invalid choice")
        else:
            task_list.pop(task_remove_input-1)
def main():
    while True:
        print("Welcome to today's todo list")
        print("1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
        start=int(input("Enter a number(1,2,3,4) : "))
        if start==1:
            add_task(task_list)
            continue
        elif start==2:
            view_task(task_list)
            continue
        elif start==3:
            remove_task(task_list)
            continue
        elif start==4:
            break
        else:
            print("Invalid choice")
            continue
        '''
        task_input=str(input("Enter task  : "))
        task_list.append(task_input)
        print(task_list)'''
main()