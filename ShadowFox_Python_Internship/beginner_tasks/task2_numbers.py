# Beginner Level - Task 2: Numbers


# ----------------------------------------
# Question 1: format() function
# ----------------------------------------

number = 145
character = "o"

result = "{} {}".format(number, character)

print("Formatted result:", result)


# ----------------------------------------
# Question 2: Circular Pond
# ----------------------------------------

radius = 84
pi = 3.14

area = pi * radius ** 2

print("Area of the pond:", area, "square meters")


# Bonus:
# 1.4 liters of water per square meter

water_per_square_meter = 1.4

total_water = area * water_per_square_meter

print("Total water in the pond:", int(total_water), "liters")


# ----------------------------------------
# Question 3: Speed
# ----------------------------------------

distance = 490
time_minutes = 7

# Convert minutes into seconds
time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed:", int(speed), "meters per second")