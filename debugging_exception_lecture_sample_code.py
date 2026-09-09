# Debugging & Exceptions Lecture Example Code 

# RunTime Error

from math import sqrt, pi

def radius(area: float) -> float:
    'calculate a circle radius given its area'
    return sqrt(area / pi)
area = float(input('enter circle area: '))
print(f'radius = {radius(area):.2f}')

# Logic Errors 

def radius(area: float) -> float:
    'calculate a circle radius given its area'
    return sqrt(area)

# Exceptions 

# def inverse() -> float:
#     """prompts user for a number & returns the inverse"""
#     number = float(input('enter a number:' ))
#     return 1 / number
# inverse()

# Preventing Exceptions 

number = float(input("enter a non-zero number: "))
while number != 0:
    print("number must be non-zero")
    number = float(input("enter a non-zero number: "))

# Handling Exceptions 

"""
try:
    statements
except: 
    statements
"""

# Handling Exceptions

try:
    number = float(input('enter a number: '))# 0 entered
    inverse = 1 / number # tries to calculate inverse using 0
    print(inverse) # prints the inverse if there is not an error
except:
    print('Error')

# Handling specific types of exceptions 

try:
    number = float(input('enter a number: '))
    inverse = 1 / number
    print(inverse)
except ValueError: # Data Type Error
    print('must enter a number')
except ZeroDivisionError: #1/0 Error
    print('number must be non-zero' )
except:
    print('an error occurred' ) # if it is not a data type of 1/0 error, print a different error

# The finally clause 

"""
try:
    statements
except ExceptionName:
    statements
finally:
    statements
"""

# Why raise exceptions? 

def calculate_new_balance(current_balance: float, withdraw_amount:float) -> float:
    if withdraw_amount <= current_balance:
        return current_balance - withdraw_amount
    else:
        raise ValueError("Withdrawal amount cannot exceed current balance")
        # withdraw more than balance
        # we don't want to allow this..
calculate_new_balance(1000.00, 1200.00)

# Why raise exceptions (2)

def get_pizza_diameter(size: str) -> int:
 """
 size - the size of the pizza: "small", "medium" or "large"
 returns the diameter of the pizza in inches
 """
 if size == 'small':
    return 10
 elif size == 'medium':
    return 12
 elif size == 'large':
    return 14
 else:
    raise ValueError("Any other word entered will not be valid")
 # anything returned here would be wrong
