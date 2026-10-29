def set_intersection(first, second):
    return sorted(set(first) & set(second))


if __name__ == "__main__":
    first = list(map(int, input("Enter first list: ").split()))
    second = list(map(int, input("Enter second list: ").split()))
    print("Intersection:", set_intersection(first, second))
