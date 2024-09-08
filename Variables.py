# Variables 
# 1. Creating a variable pi and checking its data type
pi = 22 / 7
print(type(pi))  # Outputs: <class 'float'> because 22/7 is a float division

# The following line will cause a SyntaxError:
# for = 4  
'''You will get a SyntaxError here because 'for' is a reserved keyword 
in Python, used for looping. You cannot use it as a variable name.'''

#  Calculating Simple Interest using the formula: SI = P * R * T / 100
P = 10000  # Principal amount
R = 15  # Rate of interest
T = 4  # Time in years

Simple_Interest = P * R * T / 100  # Formula for Simple Interest
print(Simple_Interest)  # Output: Simple Interest, which is 6000 in this case