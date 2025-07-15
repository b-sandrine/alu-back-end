#!/usr/bin/python3
"""
Script that fetches an employee's TODO list from a REST API
and exports it into a JSON file in a specific format.

Usage:
    python3 2-export_to_JSON.py <employee_id>
"""

import requests
import sys
import json

# ✅ Validate input
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# ✅ Define API endpoints
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

# ✅ Fetch user info
user_res = requests.get(user_url)
if user_res.status_code != 200:
    print("Employee not found.")
    sys.exit(1)

user_data = user_res.json()
username = user_data.get("username")

# ✅ Fetch TODO list
todos_res = requests.get(todos_url)
todos = todos_res.json()

# ✅ Prepare JSON structure
user_tasks = [
    {
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    }
    for task in todos
]

# ✅ Write to JSON file
filename = f"{employee_id}.json"
with open(filename, "w", encoding="utf-8") as json_file:
    json.dump({employee_id: user_tasks}, json_file)

print(f"Data exported to {filename}")
