
#2.1
#Numbers
def format_number(number, representation):
    # Using the format function to represent the number in the specified format
    formatted_str = format(number, representation)
    return formatted_str

# Test the function
result = format_number(145, 'o')
print(result)


#2.2
# Constants
pi = 3.14
radius = 84

# Calculate the area of the pond
pond_area = pi * (radius ** 2)
print(f"Area of the pond: {int(pond_area)} square meters")


# Water per square meter
water_per_square_meter = 1.4

# Total water in the pond
total_water = pond_area * water_per_square_meter

# Print the result without decimals
print(f"Total water in the pond: {int(total_water)} liters")

# Distance and time
distance = 490
time_in_seconds = 7 * 60  # Convert minutes to seconds

# Calculate speed
speed = distance / time_in_seconds

# Print the result without decimals
print(f"Speed: {int(speed)} meters per second")
