
# 'break' statement in Python

index = 1
while index <= 5:
    if index % 4 == 0:
        break
    print(index)
    index += 1
print(f'I am out of loop and value of index is {index}')


# 'continue' statement in Python
index = 0
while index <= 5:
    index += 1
    if index % 2 == 0:
        continue
    print(index)
print(f'I am out of loop and value of index is {index}')



# 'pass' statement in Python
index = 1
if index % 2 == 0:
    pass

