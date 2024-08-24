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
start_number = int(input("Enter Start number: "))
end_number = int(input("Enter End number: "))
for i in range(start_number,end_number + 1):
    if(i % 2 == 0):
        print(i)
"""
"""
ysalary = int(input("Enter Your Salary: "))
if(ysalary < 10000):
    tax = ysalary * 0.1
    result = ysalary - tax
    print("Your tax is equal : ", tax)
    print("Your salary after tax: ",result)
elif(ysalary >= 10000 and ysalary <= 30000):
    tax = ysalary * 0.15
    result = ysalary - tax
    print("Your tax is equal : ", tax)
    print("Your salary after tax: ",result)
else:
    tax = ysalary * 0.20
    result = ysalary - tax
    print("Your tax is equal : ", tax)
    print("Your salary after tax: ", result)
"""