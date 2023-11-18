# match-case in Python - same as Switch case

number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))

operator = '/'

match operator:
    case '+':
        print(number_one + number_two)
    case '-':
        print(number_one - number_two)
    case '*':
        print(number_one * number_two)
    case '/':
        print(number_one / number_two)
    case _:
        print('Unknown operator')

print('Program ended successfully ...')