"""
# 28/8/2024 form 8 to 11 pm
# ITI
"""

import json

class QueueOutOfRangeException(Exception):
    pass

class BaseQueue:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.queue_ds = []

    def insert_value(self, new_value):
        if len(self.queue_ds) >= self.size:
            raise QueueOutOfRangeException("Queue size exceeded")
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
            print("The queue is empty")
        else:
            print(self.queue_ds)

class AdvancedQueue(BaseQueue):
    queues = {}

    def __init__(self, name, size):
        super().__init__(name, size)
        AdvancedQueue.queues[name] = self

    @classmethod
    def save(cls, filename):
        data = {name: {'size': queue.size, 'queue_ds': queue.queue_ds} for name, queue in cls.queues.items()}
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Queues saved to file.")

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            cls.queues = {name: AdvancedQueue(name, info['size']) for name, info in data.items()}
            for name, info in data.items():
                cls.queues[name].queue_ds = info['queue_ds']
        print("Queues loaded from file.")