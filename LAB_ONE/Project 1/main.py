"""
# 24/8/2024 form 8 to 11 pm
# ITI
"""
while True:
    by = input("Enter your birthyear: ")
    if by.isnumeric():
        age = 2024 - int(by)
        # f {age} ---> to add var in string
        print(f"Welcome, You are {age} years old.")
        break
    else:
        print("Invalid input. Please enter a valid birth year.")