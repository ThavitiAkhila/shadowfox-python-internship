# ShadowFox Python Development Internship
# Beginner Level - Task 4: If Condition


# ========================================
# Question 1: BMI Calculator
# ========================================

print("===== BMI Calculator =====")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")


# ========================================
# Question 2 & 3: Cities and Countries
# ========================================

Australia = [
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth"
]

UAE = [
    "Dubai",
    "Abu Dhabi",
    "Sharjah",
    "Ajman"
]

India = [
    "Mumbai",
    "Bangalore",
    "Chennai",
    "Delhi"
]


def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None


# ========================================
# Find country of one city
# ========================================

print("\n===== Find Country =====")

city = input("Enter a city name: ")

country = find_country(city)

if country:
    print(city, "is in", country)
else:
    print("City not found.")


# ========================================
# Compare two cities
# ========================================

print("\n===== Compare Two Cities =====")

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = find_country(city1)
country2 = find_country(city2)

if country1 is None or country2 is None:
    print("One or both cities were not found.")
elif country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")