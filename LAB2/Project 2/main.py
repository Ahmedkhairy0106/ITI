"""
# 25/8/2024 form 8 to 11 pm
# ITI
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