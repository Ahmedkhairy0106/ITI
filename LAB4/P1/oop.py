"""
# 28/8/2024 form 8 to 11 pm
# ITI
"""

class Queue:
    def __init__(self):
        self.queue_ds = []

    def insert_value(self, new_value):
        self.queue_ds.append(new_value)
        print(f"The {new_value} is inserted into the queue.")

    def is_empty(self):
        return len(self.queue_ds) == 0

    def pop_value(self):
        if not self.is_empty():
            return self.queue_ds.pop(0)
        else:
            print("None")
            print("You tried to pop value from an empty queue")
            return None

    def display_queue(self):
        if self.is_empty():
           print("the queue is empty")
        else:
            n = self.queue_ds
            print(n)