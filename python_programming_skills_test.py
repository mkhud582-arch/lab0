# Python Programming Skills Test 

# Exercise 1 Operations 

# Ask User for cash and people input 
user_input_cash = (input("Enter an amount of cash (including $): "))
user_input_people = int(input("Enter a specified number of people:"))


user_input_cash_dollar_removal = user_input_cash.replace("$", "")
user_input_float_conversion = float(user_input_cash_dollar_removal)

# Convert dollars to pennies (1 dollar = 100 cents)

user_input_cash_cent_conversion = user_input_float_conversion * 100

# Calculate the amount of money a person receives 

money_each_person_receives = user_input_cash_cent_conversion // user_input_people

# Calculate the remaining amount of money that is leftover from splitting 

remainder_money = user_input_cash_cent_conversion % user_input_people

# Convert cash from cents back to dollars 

money_each_person_recives_cash_dollar_conversion = money_each_person_receives / 100
money_remainder_dollar_conversion = remainder_money / 100

# Print the output 

print(f"The amount of money each person they receive is: ${money_each_person_recives_cash_dollar_conversion:.2f}")
print(f"The remaining amount of money is: ${money_remainder_dollar_conversion:.2f}")
print(f"The remaining amount of money as a number of cents is {remainder_money:.2f} cents")





# Exericse 2: String Parsing

# Parsing --> XML --> Read part by part 

#file = open("log_file.txt", "w") # first argument: file name with extension, second argument: parameter 

# Read file contents
with open("log_file.txt", "r") as file: 
    for line in file:
        print(line[0:10])

closing_price = int(line[17:22]) * (1 + (int(line[24:27])/100))
    
print(closing_price)




# Exercise 3: String Methods

characters = list(input("Input the word Eric: "))
for character in characters:
    if character[0] == "E":
        lowercase_e = character[0].lower()
        lowercase_e.insert(0,character)
    elif character[1] == "R":
        lowercase_r = character[1].lower()
        lowercase_r.insert(1,character)
    elif character[2] == "I":
        lowercase_i = character[2].lower()
        lowercase_i.insert(2,character)
    elif character[3] == "C":
        lowercase_c = character[3].lower()
        lowercase_c.insert(3,character)

for character in characters:
    if character[0] == "e":
        lowercase_e = character[0].upper()
        lowercase_e.insert(0,character)
    elif character[1] == "r":
        lowercase_r = character[1].upper()
        lowercase_r.insert(1,character)
    elif character[2] == "i":
        lowercase_i = character[2].upper()
        lowercase_i.insert(2,character)
    elif character[3] == "c":
        lowercase_c = character[3].upper()
        lowercase_c.insert(3,character)

convert_characters_to_string = str(character)
print(convert_characters_to_string)



# Exercise 4: A Simple Function 

# Create the Future Value Calculation function

def future_value_calculation(PV:float, r:float, t:int) -> float:
    FV = PV * (1 + r)**t
    print(f"The Future value of the stock is ${FV:.2f} assuming a growth rate of {r * 100}% in {t} years")

user_input_present_value = input("Please input the present value of the stock (including $):")
user_input_present_value_replace_dollar = user_input_present_value.replace("$", "")

PV = float(user_input_present_value_replace_dollar)


user_input_growth_rate = (input("Please input the expected growth rate of the stock (including %):"))
user_input_growth_rate_remove_percentage = user_input_growth_rate.replace("%", "")

r = float(user_input_growth_rate_remove_percentage)


user_input_time = (input("Please input a duration needed to calculate the future value stock prices (including years):"))
user_input_remove_years = user_input_time.replace("years", "")

t = int(user_input_remove_years)

future_value_calculation(PV, r/100, t)



# Exercise 5: Nested if-else and if-elif-else 

# Ask user if they have good credit 

user_input_credit = input("Does user have good credit")

# Create a nested if-else loop that chains the conditions 

# nested if-else way 

if user_input_credit == "N":
    print("Denied")
else: 
    user_input_salary = input("Salary > 30k?")
    if user_input_salary == "N":
        print("Approve $1k")
    else: 
        user_input_age = input("Age > 30?")
        if user_input_age == "N":
            print("Approve $5k")
        else:
            print("Approve $10k")

# Create an if-elif-else conditional chain that does the same thing 

# if-elif-else way 

if user_input_credit == "N":
    print("Denied")
elif user_input_credit == "Y":
    user_input_salary = input("Salary > 30k?")
elif user_input_credit == "Y" and user_input_salary == "N":
    print("Approve $1k")
elif user_input_credit == "Y" and user_input_salary == "Y":
    user_input_age = input("Age > 30?")
elif user_input_credit == "Y" and user_input_salary == "Y" and user_input_age == "N":
    print("Approve $5k")
else:
    print("Approve $10k")


# Exercise 6: List Methods 

while True:
    user_input_numbers = list(input("Enter numbers:"))
    for nums in user_input_numbers:
        if nums[0] and len(nums) != 3:
            remove_first_number = nums.pop()
        elif len(remove_first_number) == 3:
            print(sum(remove_first_number)/len(remove_first_number))
        elif user_input_numbers == "q":
            break
        else: 
            continue

# Exercise 7: 2D Lists 

investment_data = [["Starting Value($)", "Interest Rate (%)", "Time (years)"],
                   [100.00, 5, 2], 
                   [150.00, 10, 10], 
                   [5.00, 15, 10],
                   [1,000.00, 5, 12]]

def future_value_calculation(PV:float, r:float, t:int) -> float:
    while True:
        FV = PV * (1 + r)**t
        print(f"The Future value of the stock is ${FV:.2f} assuming a growth rate of {r * 100}% in {t} years")

# Exercise 8: 2D-Lists and Loops 



board = list(list(input("Enter values into the list:")))
def tic_tac(x:int, o:int, zero:int) -> list:
    if board == 1:
        x += board
    elif board == -1:
        o += board
    elif board == 0:
        zero += board
    else:
        return ValueError

tic_tac(1,0,1)