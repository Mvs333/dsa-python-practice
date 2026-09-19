marks = [55, 89, 76, 42, 90]      # Declaration

marks.append(100)                  # Insertion at end
marks.insert(2, 60)                # Insertion at position 2

marks.remove(76)                   # Deletion by value
del marks[0]                       # Deletion by position

for index in range(len(marks)):    # Traversal
    print(index, marks[index])