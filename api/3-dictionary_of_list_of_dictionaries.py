#!/usr/bin/python3
"""
Script that fetches TODO lists for all employees from a REST API
and exports the data into a JSON file in a specified format.

Output file: todo_all_employees.json
"""

import json
import requests

# ✅ API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

# ✅ Fetch all users and todos
users = requests.get(users_url).json()
todos = requests.get(todos_url).json()

# ✅ Build the required structure
all_tasks_by_user = {}

for user in users:
    user_id = user["id"]
    username = user["username"]

    # Filter todos for the current user
    user_tasks = [
        {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in todos if task["userId"] == user_id
    ]

    # Add to dictionary
    all_tasks_by_user[str(user_id)] = user_tasks

# ✅ Export to JSON
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks_by_user, json_file)
