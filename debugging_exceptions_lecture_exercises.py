# Debugging & Exceptions Exercises 

# Exercise 1: Validating a Data Table 

def validating_data_table(table): # define my own function so that the parameter itself can be a list of lists
     for i in table:
         if len(i) == 3: 
             print("The row has elements of length 3")
         else:
             raise ValueError("The table is not a 3x3 table and is the wrong size. Please construct a valid 3x3 table.")

validating_data_table([[1,0,0],
                        [0,1,0],
                        [0,0,]
                        ])

# Exercise 2: Checking Data Types

def check_data_types(integer_parameter):
    if type(integer_parameter) == int: # compare the data type of the variable, not the variable itself
        print(f"The integer parameter entered is {integer_parameter}")
    else:
        raise TypeError(f"The value {integer_parameter} is not of type integer. Please enter a data type that is an integer.")

check_data_types("a")

# Exercise 3: Processing Values 

amts = [100.00, 50.00, 'missing', 25.00, 75.00, None]

for amt in amts:
    try:
        GST_amount = amt * 0.05
        print(f"The GST amount for float values is: {GST_amount:.2f}")
    except TypeError:
        amt = 0.00
        print(f"The GST amount for noisy or erroneous values is: {amt:.2f}")