# Strings in Python

sample_string = 'Lets learn strings in Python' # We can use Double Quote("") for string as well

multi_line = '''
    this is a
    multi-line string
    in Python 
'''

# Print a string
print(sample_string)
print(multi_line)
print(sample_string[1]) # A character can be accessed using Index

string = "python"
for char in string:
    print(char)

# Format a string using 'f'
formatted_string = f"{string} is a programming language"
print(formatted_string)

# escape Sequence
example_string = "Live the \"Life\""
print(example_string)

new_line = "line 1\nline 2"
print(new_line)


# Slicing of a String
slicing_example = 'I am ready to slice'
print(slicing_example[0:len(slicing_example)])
print(slicing_example[:])
print(slicing_example[:10])
print(slicing_example[5:])
print(slicing_example[5:10])


#Built-in functions
test_string = " python language"
print(len(test_string))
print(test_string.upper())
print(test_string.lower())
print(test_string.title()) # Upper Case Initial Characters
print(test_string.strip()) # Removes white spaces from both the end
print(test_string.split()) # By default, split based on space, accepts delimiter
print(test_string.find('python')) # Returns -1 if the item is not present
print('Python' in test_string) # Membership test
