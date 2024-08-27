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
