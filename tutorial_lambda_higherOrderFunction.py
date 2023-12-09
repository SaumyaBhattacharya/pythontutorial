# Lambda function in Python

# def square(x):
#     return x*x

square = lambda x: x*x # lambda is a keyword to create an anonymous function
print(square(3))




# HIGHER ORDER FUNCTIONS

# Function returns another function
def exponential_func(x): # Function returns another function
    return lambda n: x ** n

exp = exponential_func(2) # lambda n: 2 ** n
print(exp(3)) # lambda 3: 2 ** 3 => 8



# Function takes another function as argument
def my_map(another_func, my_list):
    return_var = []
    for item in my_list:
        transformed_item = another_func(item)
        return_var.append(transformed_item)
    return return_var

result_1 = my_map(lambda x: x+x, [1,2,3,4])
print(result_1)
result_2 = my_map(lambda x: x*x, [1,2,3,4])
print(result_2)

