# ShadowFox Python Development Internship
# Beginner Level - Task 3: List


# Initial Justice League
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Initial Justice League:")
print(justice_league)


# ----------------------------------------
# Question 1: Number of members
# ----------------------------------------

number_of_members = len(justice_league)

print("\nNumber of members:", number_of_members)


# ----------------------------------------
# Question 2: Add Batgirl and Nightwing
# ----------------------------------------

justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\nAfter adding Batgirl and Nightwing:")
print(justice_league)


# ----------------------------------------
# Question 3: Wonder Woman becomes leader
# ----------------------------------------

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\nAfter making Wonder Woman the leader:")
print(justice_league)


# ----------------------------------------
# Question 4: Separate Aquaman and Flash
# ----------------------------------------

# Move Green Lantern between Aquaman and Flash

justice_league.remove("Green Lantern")

aquaman_index = justice_league.index("Aquaman")

justice_league.insert(aquaman_index + 1, "Green Lantern")

print("\nAfter separating Aquaman and Flash:")
print(justice_league)


# ----------------------------------------
# Question 5: Create new Justice League
# ----------------------------------------

justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\nNew Justice League:")
print(justice_league)


# ----------------------------------------
# Question 6: Sort alphabetically
# ----------------------------------------

justice_league.sort()

print("\nAlphabetically sorted Justice League:")
print(justice_league)

print("\nNew leader:", justice_league[0])