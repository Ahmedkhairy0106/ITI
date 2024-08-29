"""
# 28/8/2024 form 8 to 11 pm
# ITI
"""

from oop import AdvancedQueue, QueueOutOfRangeException

queue_name = input("Enter the name of the queue: ")
queue_size = int(input("Enter the size of the queue: "))

queue_list = AdvancedQueue(queue_name, queue_size)

while True:
    operation = input(
        "[1]. Insert Into The Queue.\n[2]. Pop From The Queue.\n[3]. Check, Is It Empty Or Not.\n[4]. Display queue.\n[5]. Save Queues.\n[6]. Load Queues.\n[-1]. To Exit.\nChoose Number of Operation:\n")

    if operation not in ['1', '2', '3', '4', '5', '6', '-1']:
        print("Invalid action. Please try again.")
        continue

    if operation == '1':
        val = input("Enter Val To Insert: ")
        try:
            queue_list.insert_value(val)
        except QueueOutOfRangeException as e:
            print(e)

    elif operation == '2':
        result = queue_list.pop_value()
        if result is not None:
            print(f"The value '{result}' is popped from the queue.")

    elif operation == '3':
        v = queue_list.is_empty()
        print("Queue is empty." if v else "Queue is not empty.")

    elif operation == '4':
        queue_list.display_queue()

    elif operation == '5':
        AdvancedQueue.save("queues.txt")

    elif operation == '6':
        AdvancedQueue.load("queues.txt")

    else:
        break