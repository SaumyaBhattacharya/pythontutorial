# Type casting

num_one = input('Enter a value: ') #used to take an input from user
num_two = input('Enter another value: ')

sum = num_one + num_two
print('Incorrect result: ', sum)

sum = float(num_one) + float(num_two) #Explicit type casting [string -> float]
print('Correct result: ', sum)


