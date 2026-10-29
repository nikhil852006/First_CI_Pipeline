def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    return sorted(first) == sorted(second)


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    print("Are anagrams:", is_anagram(first, second))
