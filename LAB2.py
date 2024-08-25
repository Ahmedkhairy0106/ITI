"""
# 25/8/2024 form 8 to 11 pm
# ITI
"""

"""
# Create an empty dictionary
users = {}

def calculate_average_age(ages):
    if len(ages) == 0:
        return 0
    return sum(ages) / len(ages)

while True:
    username = input("Enter Username or '-1' to terminate program):\n")
    if username == '-1':
        break
    # Get input from the user
    age = input("ENTER YOUR AGE: \n")
    if username.isalpha() and age.isnumeric():
        # Store the input in the dictionary
        users[username] = int(age)
    else:
        print("Sorry, Enter valid User name or Age...")

# Calculate and print the average age
average = calculate_average_age(users.values())
print(f"\nThe average age is {average}")
"""

"""
import json
import random

def generate_random_number():
    random_numbers = [random.randint(1,100) for _ in range(10)]

    with open("numbers.txt", "w") as f:
        json.dump(random_numbers,f)
        print("NUMBER IN FILES: ")
        print(random_numbers)

def sort_numbers_from_file():
    numbers = []

    with open("numbers.txt", "r") as f:
        numbers = json.load(f)

    sorted_number = sorted(numbers)

    with open("sorted_numbers.txt", "w") as f:
        json.dump(sorted_number,f)
        print("\nNumber was added and sorted successfully")


generate_random_number()

sort_numbers_from_file()

"""