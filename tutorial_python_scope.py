# Scopes in Python

# Example 1

global_variable = 1 # Variable can be accessed throughout the program
def sample_func():
    local_variable = 2 # Local variable can't be accessed from outside
    print('Local variable: ', local_variable)
    print('Global variable: ', global_variable)

sample_func()
#print('local variable: ',local_variable) # Not accessable
print('Global variable: ', global_variable)
print('--------------------------------------------------------')


# Example 2

item = 1
def my_func():
    global item # We can access global variable from local scope
    item = 7
    print('Global variable from local scope: ', item) #7
my_func()
print(item) #7
print('-------------------------------------------------------')


# Example 3

item = 1    # Global scope
def outer_func():
    item = 2    # Nonlocal compared to inner_func()
    print('From outer function: ', item) #2
    def inner_func():
        nonlocal item
        item = 3    # Local scope
        print('From inner function: ', item) #3

    inner_func()
    print('nonlocal variable changed: ', item) #3
outer_func()
print('Global scope: ', item) #1