#Set in Python

first_set = {2, 7, 9}
second_set = {2, 4, 6, 10}

print(type(first_set))

# Print the sets
print(first_set)

for item in first_set:
    print(item)

# We can NOT use index to print element of a Set
print(first_set[0])

# Built-in functions of Set
print(len(second_set))

first_set.add(11)
print('First set after adding 11:', first_set)

second_set.remove(10) # Throws error if the item is not present
second_set.discard(100) # Do not throw error if the item is not present
print('Second set after removing 10:', second_set)

# Mathematical operations
print('Set one: ', first_set)
print('set two: ', second_set)
print('Union of two sets: ', first_set.union(second_set))
print('Intersection of two sets: ', first_set.intersection(second_set))
print('Difference: ', first_set.difference(second_set))
print('Symmetric difference: ', first_set.symmetric_difference(second_set))

first_set.clear() # Result set will be an empty set
print(first_set)

