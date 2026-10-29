def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Armstrong number:", is_armstrong(number))
