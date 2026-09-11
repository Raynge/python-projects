import time

data = {}

# =================================
# FUNCTIONS
# =================================


def found():
    print()
    print('Searching...')
    print()
    time.sleep(1.3)
    print('FOUND...')
    print()


def not_found():
    print()
    print('Searching...')
    print()
    time.sleep(1.3)
    print('NAME NOT FOUND...')
    print()
    time.sleep(1.3)
    print('REDIRECTING...')
# =================================


def main_program():
    while True:
        try:
            print()
            print('===== Student Score Manager =====')
            print()
            print('1. Add student', '2. Find student', '3. Update score',
                  '4. Delete student', '5. Show all students', '6. Exit', sep='\n')
            print('=================================')
            choice = int(input('Choice: '))

            if choice <= 0 or choice > 6:
                print('Choose a number in the given option range.')
                continue
            else:
                break

        except ValueError:
            print()
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('Please choose a valid option.')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    return choice

# =================================


def add_student():
    student = input('Enter the name of the student: ')

    while True:
        try:
            score = int(input(f"Enter {student}'s score: "))
            break
        except ValueError:
            print()
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('Please choose a valid option.')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

    data[student] = score
    print()
    print('Data added successfully.')


def find_student():
    name_to_search = input("Student's name (CASE SENSITIVE): ")

    if name_to_search in data:
        found()
        print('====Current Data====')
        print(f'{name_to_search}:{data[name_to_search]}')
        print('====================')

    else:
        not_found()


def update_score():
    name_to_update = input("Student's name (CASE SENSITIVE): ")

    if name_to_update not in data:
        not_found()

    else:
        found()
        print(f'Current Data -> {name_to_update}:{data[name_to_update]}')
        print("=================================")

        while True:
            try:
                new_score = int(input('Enter New Score: '))
                data[name_to_update] = new_score
                break
            except ValueError:
                print()
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print('Please choose a valid option.')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

        print()
        print('Score updated successfully')
        time.sleep(1.3)


def del_student():
    name_to_delete = input("Student's name (CASE SENSITIVE): ")

    if name_to_delete not in data:
        not_found()

    else:
        found()
        print(f'Current Data -> {name_to_delete}:{data[name_to_delete]}')
        print("=================================")

        confirmation = input(
            f"Are you sure you want to delete {name_to_delete}'s Data(y/n): ").lower()

        if confirmation == 'y' or confirmation == 'yes':
            del data[name_to_delete]
            print('Name successfully deleted.')
        else:
            print('Name was NOT deleted.')


def view_students():
    if data:
        print('Searching...')
        time.sleep(1.3)
        print('Processing...')
        time.sleep(1.2)
        print()
        print('======== ALL STUDENTS ========')
        print()

        for student in data:
            print(f'{student}: {data[student]}')
        print()
        print('==============================')

    else:
        print('No Data to display...')


# =================================
# MAIN PROGRAM
# =================================
while True:
    choice = main_program()

    if choice == 1:
        print()
        add_student()
        time.sleep(1.2)

    elif choice == 2:
        print()
        find_student()
        time.sleep(1.2)

    elif choice == 3:
        print()
        update_score()
        time.sleep(1.2)

    elif choice == 4:
        print()
        del_student()
        time.sleep(1.2)

    elif choice == 5:
        print()
        view_students()
        input('Press Enter to return to Menu...')

    else:
        print('Aight cya!')
        break
