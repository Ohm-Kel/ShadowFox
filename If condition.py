# 4.1
# If Condition
# User input for height in meters
height = float(input('Enter height in meters:\n'))

# User input for weight in kilograms
weight = int(input('Enter weight in kilograms:\n'))

# Calculate BMI using the formula: weight / (height ** 2)
BMI = weight / (height ** 2)

# Determine and print the BMI category based on the calculated BMI value

if BMI >= 30:
    # If BMI is 30 or more, classify as 'Obesity'
    print("Obesity")
elif BMI > 25 < 29:
    # This condition checks if BMI is between 25 and 29 (exclusive),
    # It should be BMI > 25 and BMI <= 29 to be correct
    print("Overweight")
elif BMI > 18.5 < 25:
    # This condition checks if BMI is between 18.5 and 25 (exclusive),
    # It should be BMI > 18.5 and BMI <= 25 to be correct
    print('Normal')
elif BMI < 18.5:
    # If BMI is less than 18.5, classify as 'Underweight'
    print("Underweight")

# 4.2

# Define the lists of cities for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter a city name
city = input("Enter a city name: ")

# Determine which country the city belongs to
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")

#f Condition
#4.3
# Define the lists of cities for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two cities
city_1 = input("Enter the first city: ")
city_2 = input("Enter the second city: ")

# Determine if both cities are in the same country
if city_1 in australia and city_2 in australia:
    print("Both cities are in Australia")
elif city_1 in uae and city_2 in uae:
    print("Both cities are in UAE")
elif city_1 in india and city_2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")