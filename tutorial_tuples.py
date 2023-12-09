# Tuples in Python
employee_one = ('Ram', 32, '20-Nov-2023')

print(employee_one)

for item in employee_one:
    print(item)

print(f'Age of the employee {employee_one[1]}')

# Tuple is immutable - below operation is not possible
#employee_one[1] = 100


# Built-in functions of Tuple in Python
numbers_tuple = (2, 5, 1, 5)

print(f'Length of the tuple: {len(numbers_tuple)}')
print(f'Maximum elements of a tuple: {max(numbers_tuple)}')
print(f'First occurrence of 5: {numbers_tuple.index(5)}')
print(f'Count of 5 in the tuple: {numbers_tuple.count(5)}')
