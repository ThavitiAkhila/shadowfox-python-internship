# ShadowFox Python Development Internship
# Beginner Level - Task 5: For Loop


import random


# ========================================
# Question 1: Rolling a Dice
# ========================================

print("===== Dice Rolling Simulation =====")

six_count = 0
one_count = 0
two_sixes_in_row = 0

previous_roll = None

for i in range(20):

    roll = random.randint(1, 6)

    print("Roll", i + 1, ":", roll)

    if roll == 6:
        six_count += 1

    if roll == 1:
        one_count += 1

    if previous_roll == 6 and roll == 6:
        two_sixes_in_row += 1

    previous_roll = roll


print("\nNumber of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s occurred in a row:", two_sixes_in_row)


# ========================================
# Question 2: Jumping Jacks
# ========================================

print("\n===== Jumping Jacks =====")

completed = 0

for i in range(10):

    completed += 10

    print("\nYou completed", completed, "jumping jacks.")

    if completed == 100:
        print("Congratulations! You completed the workout!")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":

        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks.")
            break

    remaining = 100 - completed

    print("You have", remaining, "jumping jacks remaining.")