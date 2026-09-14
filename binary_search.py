def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

scores = [10, 25, 40, 55, 70, 85, 95]
result = binary_search(scores, 70)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")