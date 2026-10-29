def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers), min(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    maximum, minimum = find_max_min(numbers)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
