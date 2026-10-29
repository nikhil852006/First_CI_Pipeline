def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)
    return items[-k:] + items[:-k] if k else items[:]


if __name__ == "__main__":
    items = input("Enter items separated by spaces: ").split()
    k = int(input("Enter rotation count: "))
    print("Rotated list:", rotate_list(items, k))
