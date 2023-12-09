# List in Python - can store multiple values in a single variable
sample_list = [2, 'Bangalore', 5.7, True]

print(sample_list)

for item in sample_list:
    print(item)


# Fetching values from a List
print(sample_list[0])
print(sample_list[2])
print(sample_list[-1]) # Negative indexes
print(sample_list[-2])



# Slicing of a List
numbers = [2, 5, 1, 6, 3]

print(numbers[0: len(numbers)])
print(numbers[:]) # By default, initial index is 0 & end index is len(list)
print(numbers[1: 3]) # prints from 1st index to 2nd index, not till 3rd index
print(numbers[1:])
print(numbers[:3])
print(numbers[1:5:2]) # :2 is the step size

# Built-in functions for List
numbers = [2, 5, 1, 6, 3]
print(f'Length of the List is {len(numbers)}')
print(f'Maximum element of a List is {max(numbers)}')
# Below built-in functions modify the existing list
numbers.sort()
print(f'Sorted list : {numbers}')
numbers.append(0)
print(f'Appended List: {numbers}') # Insert at the last
print(f'Popped element: {numbers.pop()}') # removes the last element
print(numbers)
numbers.extend([8,9])
print(f'append new list within the existing list: {numbers}')
numbers.reverse()
print(f'List is reversed: {numbers}')

