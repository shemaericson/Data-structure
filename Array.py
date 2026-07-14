# Time Complexity:
# Read: O(1)
# Update: O(1)
# Traverse: O(n)
# Find Max: O(n)
# Insert: O(n)

marks = [70, 85, 90, 60, 75]

print("Original Array:", marks)

# Read
index = 2
print("Value at index", index, "=", marks[index])

# Update
marks[3] = 95
print("After Update:", marks)

# Traverse
print("All Marks:")
for mark in marks:
    print(mark)

# Maximum
maximum = marks[0]
for mark in marks:
    if mark > maximum:
        maximum = mark
print("Maximum:", maximum)

# Insert without built-in insert
new_value = 80
insert_index = 2

print("Before Insertion:", marks)

marks.append(0)

for i in range(len(marks)-1, insert_index, -1):
    marks[i] = marks[i-1]

marks[insert_index] = new_value

print("After Insertion:", marks)
