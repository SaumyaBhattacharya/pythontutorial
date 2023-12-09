# Loops in Python
# Print same string 20 times

index = 0 # Initialization

while index < 20: # Condition
    print('I am learning Python')
    index = index + 1
else: # Else is optional, you may not use it if it is not required
    print('I have learned Python') # This execute only once



#Using for loop

for index in range(20):
    print('I am learning Python')
else:
    print('I have learned Python')








# Print all even numbers from 1 to 10

number = 1

while number <= 10:
    if number%2 == 0:
        print(number, ' ')
    number += 1 # number = number + 1


# Infinite loop

number = 1
while number == 1:
    print('I am an infinite loop...')
