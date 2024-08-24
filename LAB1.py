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
"""

"""
while True:
    start_number = input("Enter Start number: ")
    end_number = input("Enter End number: ")

    if start_number.isnumeric() and int(start_number) >= 0:
        if start_number.isdigit() and end_number.isdigit():
            for i in range(int(start_number), int(end_number) + 1):
                if i % 2 == 0:
                   print(i)
            break
        else:
           print("Invalid input. Please enter a valid input.")
    else:
        print("Please enter a positive start.")

"""

"""
while True:
    ysalary = input("Enter Your Salary: ")
    if ysalary.isnumeric():
        ysalary = int(ysalary)
        if ysalary < 10000:
            tax = int(ysalary) * 0.1
        elif ysalary >= 10000 and ysalary <= 30000:
            tax = int(ysalary) * 0.15
        else:
            tax = int(ysalary) * 0.20

        result = int(ysalary) - tax
        print("Your tax is equal: ", tax)
        print("Your salary after tax: ", result)
        break
    else:
        print("Invalid input. Please enter a valid salary.")
"""
