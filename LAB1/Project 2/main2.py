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
