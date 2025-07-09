#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get user info
    user_res = requests.get(user_url)
    if user_res.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_res.json()
    employee_name = user_data.get("name")

    # Get TODOs
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print results
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

