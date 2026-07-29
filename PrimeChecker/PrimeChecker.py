import math


def prime_checker():
    while True:
        try:
            number = int(input("Enter your number: "))
            break
        except ValueError:
            print("Please enter a valid number (not decimal).")

    is_prime = True

    if number < 2:
        print(f"{number} is not a prime.")

    else:
        for i in range(2, int(math.sqrt(number)) + 1):

            if number % i == 0:
                is_prime = False
                print(f"{number} is not a prime.")
                break

        if is_prime:
            print(f"{number} is a prime.")


while True:
    prime_checker()
    redo = input("Do you wanna go again? (y/n): ").strip().lower()
    if redo != 'y':
        print('Aight have a good day!')
        break
