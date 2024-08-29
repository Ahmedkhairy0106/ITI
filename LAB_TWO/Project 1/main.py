"""
# 25/8/2024 form 8 to 11 pm
# ITI
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

