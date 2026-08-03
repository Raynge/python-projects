tasks = []

# =================================
# FUNCTIONS
# =================================


def add_task():
    while True:
        try:
            print()
            task_number = int(
                input('How many tasks do you want to enter?: '))
            print()
        except ValueError:
            print("Please enter a valid number.")
            continue

        if task_number <= 0:
            print('Please enter a positive number.')
            continue
        else:
            break

    for i in range(task_number):
        tasks.append(input(f'Task {i + 1}: ').strip())


def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task}')


def remove_task():
    while True:
        try:
            print()
            tasks_to_remove = int(
                input('How many tasks do you want to remove?: '))
            print()
        except ValueError:
            print("Please enter a valid number.")
            continue

        if tasks_to_remove <= 0:
            print('Please enter a positive number.')
            continue
        else:
            break

    for i in range(tasks_to_remove):
        try:
            task_index = int(
                input('Task you want to remove(number): ')) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print(f'Removed task number {task_index + 1}')
        else:
            print(f'Invalid task number. (No. of Tasks -> {len(tasks)})')


def main_prompt():
    while True:
        try:
            print()
            print('=================================')
            print('Pick an option:')
            print('=================================')
            print('1. Add a task', '2. Remove a task',
                  '3. View tasks', '4. Exit', sep='\n')
            print('=================================')
            option = int(input('Choice: '))
            break
        except ValueError:
            print("Please enter a valid number.")
    return option

# =================================
# MAIN PROGRAM
# =================================


while True:
    option = main_prompt()

    if option == 1:
        add_task()

    elif option == 2:
        print()

        if len(tasks) == 0:
            print('No tasks to remove.')
            continue

        else:
            view_tasks()
            remove_task()

    elif option == 3:
        print()

        if len(tasks) == 0:
            print('No tasks available.')
        else:
            print('=================================')
            view_tasks()
            print('=================================')

    elif option == 4:
        print('Aight have a good day!')
        break
    else:
        print('Please enter a number within the given range. (1-4)')
