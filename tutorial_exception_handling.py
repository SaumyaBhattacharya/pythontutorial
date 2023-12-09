# Exception Handling in Python

# dividend = int(input('Enter a dividend: '))
# divisor = int(input('Enter a divisor: '))
# try:
#     result = dividend / divisor # 5/0
#     print(f'result is {result}')
#
# except Exception:
#     print("Exception occurred")
#
# else:
#     print('Division operation is successful...')
#
# finally:
#     print('Program ended successfully...')






# Custom Exception:
# class InvalidAgeException(Exception):
#     pass
#
# age = int(input('Enter your age: '))
#
# try:
#     if age < 18:
#         raise InvalidAgeException
#     else:
#         print('Eligible for vote')
# except InvalidAgeException:
#     print('Exception: Invalid Age!')




# Multiple 'except' blocks

dividend = input('Enter a dividend: ')
divisor = input('Enter a divisor: ')
try:
    result = int(dividend) / int(divisor)
    print(f'result is {result}')


except ValueError:
    print("Value entered is not an integer")

except ZeroDivisionError:
    print("Divisor can not be 0")

except Exception:
    print("Exception occurred")

else:
    print('Division operation is successful...')

finally:
    print('Program ended successfully...')


