from queue import Queue
import random

queue = Queue()

def generate_request():
    """Generate random request"""
    request_id = random.random()
    queue.put({"id": request_id, "name": f"Request N{round(request_id, 3)}"})

def process_request():
    """Process request"""
    if not queue.empty():
        request = queue.get()
        print(f"Request with id {request.get("id")} processed.")
    else:
        print("Queue is empty")

while True:
    answer = input("Do you want to exit (y/n)? ")
    if answer.lower().strip() == "n":
        generate_request()
        process_request()
    else:
        break
