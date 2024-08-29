"""
# 28/8/2024 form 8 to 11 pm
# ITI
"""
from oop import Queue  # Import the Queue class

queue_list = Queue()  # Create an instance of the Queue class

while True:
    operation = input("[1]. Insert Into The Queue.\n[2]. Pop From The Queue.\n[3]. Check, Is It Empty Or Not.\n[4]. Display queue.\n[-1]. To Exit.\nChoose Number of Operation:\n")
    if operation not in ['1', '2', '3','4', '-1']:
        print("Invalid action. Please try again.")
        continue

    if operation == '1':
        val = input("Enter Val To Insert: ")
        queue_list.insert_value(val)

    elif operation == '2':
        result = queue_list.pop_value()
        if result is not None:
            print(f"The value '{result}' is popped from the queue.")

    elif operation == '3':
        v = queue_list.is_empty()
        print("Queue is empty." if v else "Queue is not empty.")

    elif operation == '4':
        queue_list.display_queue()

    else:
        break