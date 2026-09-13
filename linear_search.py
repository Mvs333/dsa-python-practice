def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1

marks = [55, 89, 76, 42, 90]
result = linear_search(marks, 76)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")