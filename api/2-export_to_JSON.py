#!/usr/bin/python3
"""
Script that fetches all users' TODO lists from a REST API
and exports the data into a JSON file (todo_all_employees.json).
"""

import requests
import json

# ✅ API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# ✅ Fetch all users and todos
users = requests.get(users_url).json()
todos = requests.get(todos_url).json()

# ✅ Prepare the output structure
all_data = {}

for user in users:
    user_id = user["id"]
    username = user["username"]
    
    # Filter todos for this user
    user_tasks = [todo for todo in todos if todo["userId"] == user_id]

    # Build the task list for this user
    all_data[str(user_id)] = [
        {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in user_tasks
    ]

# ✅ Write to JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_data, json_file, indent=4)

print("Data exported to todo_all_employees.json")
