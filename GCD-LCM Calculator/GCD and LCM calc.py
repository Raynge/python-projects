def gcd(first_number, second_number):
    while second_number != 0:
        remainder = first_number % second_number
        first_number = second_number
        second_number = remainder
    return first_number


def lcm(first_number, second_number):
    gcd_numbers = gcd(first_number, second_number)
    lcm_numbers = (first_number * second_number) // gcd_numbers
    return lcm_numbers


redo = True

while redo:

    while True:
        try:
            print()
            first_number = int(input("Enter your first number: "))
            second_number = int(input("Enter your second number: "))
            print()
            print("1. GCD", "2. LCM", "3. Both", sep="\n")
            print()
            operation = int(input("Choice: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if operation == 1:
        gcd_numbers = gcd(first_number, second_number)
        print()
        print(f"HCF / GCD : {gcd_numbers}")

    elif operation == 2:
        lcm_numbers = lcm(first_number, second_number)
        print()
        print(f"LCM : {lcm_numbers}")

    elif operation == 3:
        gcd_numbers = gcd(first_number, second_number)
        lcm_numbers = lcm(first_number, second_number)
        print()
        print(f"HCF / GCD : {gcd_numbers}")
        print(f"   LCM    : {lcm_numbers}")

    else:
        print("Please choose a valid operation (1,2,3).")
        continue

    print()
    retry = input("Do you wanna go again? (y/n): ").strip().lower()
    redo = True if retry == 'y' else False
