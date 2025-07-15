#!/usr/bin/python3

""" Module documentation: This file contains the
 codes that fetch data from 2 apis and console the completed
tasks on the console """

import requests
import sys

# ✅ Validate input
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# ✅ Define API endpoints
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

# ✅ Fetch user data
user_res = requests.get(user_url)
if user_res.status_code != 200:
    print("Employee not found.")
    sys.exit(1)

user_data = user_res.json()
employee_name = user_data.get("name")

# ✅ Fetch TODO list
todos_res = requests.get(todos_url)
todos = todos_res.json()

# ✅ Count total and completed tasks
total_tasks = len(todos)
done_tasks = [task for task in todos if task.get("completed")]
num_done = len(done_tasks)

# ✅ Print required format
print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")

for task in done_tasks:
    print(f"\t {task.get('title')}")
