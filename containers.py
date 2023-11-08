# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

# your solution here

students = ["Nisal", "Nick", "Krystalin", "Chris", "Ahmad", "Kevin"]

print(students[1])
print(students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "[food goes here] is a good food".

# your solution here

foods = ("pizza", "burger", "fries", "chicken", "poutine", "burrito")

for food in foods:
    print(f'{food} is a good food')

# Exercise 3
# Using a for loop, print just the last two food strings from foods.

# your solution here

for food in foods[-2:]:
    print(food)

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

# your solution here

home_town = {
    "city": "New York", 
    "state": "NY", 
    "population": 7888121
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# Exercise 5

# your solution here


# Exercise 6

# your solution here


# Exercise 7

# your solution here


# Exercise 8

# your solution here
