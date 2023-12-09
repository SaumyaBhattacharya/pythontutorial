# Dictionary in Python
lang_creator_dict = {'python': 'Rossum', 'c': 'Ritchie', 'java': 'Gosling'}


# Print the dict
print(lang_creator_dict)

print('Python language created by: ', lang_creator_dict['python'])
print('Java language created by: ', lang_creator_dict.get('java'))

for key, value in lang_creator_dict.items():
    print(key, '->', value)


# Dict is mutable
lang_creator_dict['c'] = 'Dennis Ritchie'
print(lang_creator_dict)


# Built-in functions
print(f'length of the dict {len(lang_creator_dict)}')

print(f'Keys are: {lang_creator_dict.keys()}')
print(f'Values are: {lang_creator_dict.values()}')
print(f'Dict items are: {lang_creator_dict.items()}')

lang_creator_dict.pop('c')
print(lang_creator_dict)
lang_creator_dict.popitem()
print(lang_creator_dict)
lang_creator_dict.clear()
print(lang_creator_dict)
