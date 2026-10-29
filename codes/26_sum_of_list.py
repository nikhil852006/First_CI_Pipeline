def sum_of_list(numbers):
    return sum(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sum:", sum_of_list(numbers))
