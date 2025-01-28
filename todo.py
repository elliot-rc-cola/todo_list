# todo list manager
# user can add, view and remove tasks
### would be nice if the user could also view and restore deleted tasks
# use a count to add a number to each list item so they're easier for the user to remove (or add back)
### could we do this with indicies instead, that way if items aren't removed sequentially there won't be gaps in the numbering
# it would make sense for the program to create a file to store the list otherwise it would be lost each time you exit...
### we'll start by using lists to get the logic right, then add the filehandling
#let's get into it!


#fuctions for adding, removing and restoring tasks

# the todo manager
def todo_manager():

    #the lists
    todo_list = []
    removed_list = []

    # while loop menu
    while True:
        print('\nTo-Do List')
        print('1. Add a task')
        print('2. View tasks')
        print('3. Remove a task')
        print('4. View completed tasks')
        print('5. Restore a task')
        print('6. Exit')

        choice = input('Choose an option: ')

        # adding to the list
        if choice == '1':
            task = input('Add... ')
            todo_list.append(task)

        # viewing the active todo's
        elif choice == '2':
            if todo_list == []:
                print('Your list is empty.')
            else:
                print('Active Tasks:')
                for task in todo_list:
                    print(f'- {task}')

        # removing a task
        elif choice == '3':
            if not todo_list:
                print('Your list is empty.')
            else:
                remove = input('Remove... ')
                try:
                    todo_list.remove(remove)
                    removed_list.append(remove)
                except ValueError:
                    print("Error: That item isn't on the list")

        # viewing completed todo's
        elif choice == '4':
            if not removed_list:
                print('Your list is empty.')
            else:
                print('Completed Tasks:')
                for task in removed_list:
                    print(f'- {task}')

        # restoring a task from the completed list
        elif choice == '5':
            restore = input('Restore... ')
            try:
                removed_list.remove(restore)
                todo_list.append(restore)
                print(f'Task "{restore}" has been restored')
            except ValueError:
                print("Error: That item isn't on the list")

        # ending the program
        elif choice == '6':
            print('Keep up the good work!')
            break

        # handling any input errors
        else:
            print('Error: Please type the number for the corresponding task')
            print("To add a task type '1'")
            choice = input('Choose an option: ')


#calling the menu
todo_manager()