# File Handling in Python

# file = open('programming_lang.txt', 'r')
# print('File content:\n', file.read()) # Reads the whole content together
# print('File name: ', file.name) # We can get the file name
# print('File open mode: ', file.mode) # We can get the file open mode
# file.close()    # We need to close the file at the end






# Best practice - No need to remember/write "file.close()"

# with open('programming_lang.txt', 'r') as file:
#     print('File content:\n', file.readlines())
#     print('File name: ', file.name)
#     print('File open mode: ', file.mode)














# Read part of a file at a time - Works for large files
# with open('programming_lang.txt', 'r') as file:
#     data_chunk = file.read(10) # Reads 10 characters at a time
#     while len(data_chunk) != 0: # End of file(EOF) will have no character
#         print(data_chunk)
#         data_chunk = file.read(10)









# tell() & seek() functions
# with open('programming_lang.txt', 'r+') as file:
#     print(file.read())
#     print('File pointer location: ', file.tell())
#     file.seek(0)
#     file.write('Zython')








# File copy Operation
# programming_lang.txt => programming_lang_copy.txt

with open('programming_lang.txt', 'r') as read_file:
    with open('programming_lang_copy.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)










