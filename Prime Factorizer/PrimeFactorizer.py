def prime_factorizer():
    prime_factors = []

    while True:
        try:
            number = int(input("Enter your number: "))
            break
        except ValueError:
            print("Please enter a valid number (not decimal).")

    new_number = number

    for divior in range(2, number//2 + 1):
        while new_number % divior == 0:
            prime_factors.append(divior)
            new_number //= divior

        if new_number == 1:
            break

    if new_number == number:
        prime_factors.append(number)

    return number, prime_factors

# ==================================================================


number, prime_factors = prime_factorizer()

print(f'The prime factors of {number} are --> {prime_factors}')
