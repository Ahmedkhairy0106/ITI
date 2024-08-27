import json
import random
import time
from time import sleep
from turtledemo.penrose import start


def calculate_time(inner_function):
    def wrap(*args,**kwargs):
        start = time.time()
        inner_function(*args,**kwargs)
        end = time.time()
        print("Function time is", end - start, "s")
    return wrap

def generate_random_number():
    random_numbers = [random.randint(1,100) for _ in range(10)]

    with open("numbers.txt", "w") as f:
        json.dump(random_numbers,f)
        print("NUMBER IN FILES: ")
        print(random_numbers)

@calculate_time
def sort_numbers_from_file():
    numbers = []

    with open("numbers.txt", "r") as f:
        numbers = json.load(f)

    sorted_number = sorted(numbers)
    sleep(1)
    with open("sorted_numbers.txt", "w") as f:
        json.dump(sorted_number,f)
        print("\nNumber was added and sorted successfully")


generate_random_number()

sort_numbers_from_file()