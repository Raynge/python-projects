import time

# =================================
# FUNCTIONS
# =================================


def main_program():
    while True:
        try:
            print()
            print('=================================')
            print('Pick an option:')
            print('=================================')
            print('1. Add a contact', '2. Remove a contact',
                  '3. View contacts', '4. Exit', sep='\n')
            print('=================================')
            option = int(input('Choice: '))

            if option not in [1, 2, 3, 4]:
                print('Please choose a valid option')
                continue

            break

        except ValueError:
            print('Please choose a valid option')

    return option

# =================================


def lines_counter():
    lines = 0
    with open('contacts.txt') as file:
        for line in file:
            lines += 1

    return lines
# =================================


def add_contact():
    name = input('Enter the name: ')
    phone = input('Number: ')

    with open('contacts.txt') as file1:
        found = False
        for line in file1:
            dupe_name, phone2 = line.strip().split(',')

            if dupe_name == name:
                found = True
                break

        if found:
            print('Contact under the given name already exists.')
        else:
            with open('contacts.txt', 'a') as file2:
                lines = lines_counter()
                if lines != 0:
                    file2.write(f'\n{name}, {phone}')
                else:
                    file2.write(f'{name}, {phone}\n')

            print('Contact added successfully.')

# =================================


def remove_contact():
    name = input('Enter the name: ')

    with open('contacts.txt') as file:
        found = False
        content = []

        for line in file:
            dupe_name, phone2 = line.strip().split(',')

            if dupe_name == name:
                found = True

            else:
                content.append(line)

        if found == False:
            print(f'No contact with the name {name} is available.')

        else:
            with open('contacts.txt', 'w') as file:

                for line in content:
                    file.write(line)
            print('Contact removed successfully.')

# =================================


def view_contacts():
    with open('contacts.txt') as file:
        for line in file:
            name, phone = line.strip().split(',')
            print(f'{name} : {phone}')


# =================================
# MAIN PROGRAM
# =================================

while True:
    option = main_program()

    if option == 1:
        print()
        add_contact()
        time.sleep(3)

    elif option == 2:
        print()
        remove_contact()
        time.sleep(3)

    elif option == 3:
        lines = lines_counter()

        if lines == 0:
            print('No contacts available.')
            time.sleep(3)
        else:
            print()
            view_contacts()
            print()
            time.sleep(3)

    else:
        break
