# =================================
# FUNCTIONS
# =================================

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


# =================================
# MAIN PROGRAM
# =================================

redo = True

while redo:

    while True:
        try:
            print()
            print("1. GCD", "2. LCM", "3. Both",
                  "4. Fraction simplifier",   sep="\n")
            print()
            operation = int(input("Choice: "))
            print()

            if operation != 4:
                first_number = int(input("Enter your first number: "))
                second_number = int(input("Enter your second number: "))

            break
        except ValueError:
            print("Please enter a valid number.")

    # =================================

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

    elif operation == 4:
        numerator = int(input('Numerator: '))
        denominator = int(input('Denominator: '))
        if denominator == 0:
            print("Denominator cannot be zero.")
        else:
            gcd_numbers = gcd(numerator, denominator)
            print()
            print(
                f'{numerator}/{denominator} : {numerator//gcd_numbers}/{denominator//gcd_numbers}')

    else:
        print("Please choose a valid operation (1,2,3, 4).")
        continue

# =================================

    print()
    retry = input("Do you wanna go again? (y/n): ").strip().lower()
    redo = True if retry == 'y' else False
