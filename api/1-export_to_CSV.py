#!/usr/bin/python3
"""
Script that fetches an employee's TODO list from a REST API
and exports it into a CSV file.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys
import csv

# ✅ Validate command-line arguments
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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
employee_username = user_data.get("username")

# ✅ Fetch TODOs
todos_res = requests.get(todos_url)
if todos_res.status_code != 200:
    print("Failed to fetch TODOs.")
    sys.exit(1)

todos = todos_res.json()

# ✅ Prepare CSV filename
file_name = f"{employee_id}.csv"

# ✅ Write to CSV file
with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    for task in todos:
        writer.writerow([
            employee_id,
            employee_username,
            str(task.get("completed")),
            task.get("title")
        ])

print(f"Data exported to {file_name}")

