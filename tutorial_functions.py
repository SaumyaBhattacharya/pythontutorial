# Function to perform task
def greet():                    # Function definition
    print('Hello there...')


greet()                         # calling the function



# Function with return keyword
# def greet():
#     return 'Hello there...'
#
#
# return_value = greet()
# print(return_value)



# Function with Parameters

def division(dividend, divisor):
    return dividend / divisor


result = division(4,2)
print(result)



# # Function with Parameters - Keyword Argument
# def division(dividend, divisor):
#     return dividend / divisor
#
#
# result = division(divisor=2, dividend=4)
# print(result)




# #Default arguments - Optional parameters
# def division(dividend, divisor=2):
#     return dividend / divisor
#
#
# result_with_one_arg = division(4)
# print(result_with_one_arg)
# result_with_all_args = division(9,3)
# print(result_with_all_args)




# Variable arguments - Non-keyword arguments
def sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


result = sum(2, 4, 5, 7, 8)
print(result)


# Variable arguments - Keyword arguments
def var_args(**kwargs):
    print(kwargs)


var_args(name='Ram', id=101)