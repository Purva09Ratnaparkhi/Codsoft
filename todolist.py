tasks = []

def add(task):
    tasks.append(task)
    print("\nTask added successfully!")
    
def update(index,new_task):
    if index <= len(tasks):
        tasks[index - 1] = new_task
        print("Task updated successfully!")
    else:
        print("You have given invalid task index.")
        
def display():
    if tasks:
        print("\nTasks in To-Do-List:")
        for index, task in enumerate(tasks):
            print(f"{index+1}.{task}")
    else:
        print("No tasks in the list.")
        
def delete(index):
    if index <= len(tasks):
        del tasks[index - 1]
        print("Task removed successfully!")
    else:
        print("You have given invalid task index.")
    
        
while True:
    print("\n*** To-Do-List ***")
    print("1.Add Task\n2.Update Task\n3.Display Task\n4.Delete\n5.Exit")
    choice = input("\nEnter your choice: ")
    
    match choice:
        case '1':
            task = input("Enter the task: ")
            add(task)
        
        case '2':
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update(index, new_task)
            
        case '3':
            display()
            
        case '4':
            index = int(input("Enter the task index to delete: "))
            delete(index)
            
        case '5':
            break
        
        case _:
            print("Invalid choice. Please try again.")
                
            
    