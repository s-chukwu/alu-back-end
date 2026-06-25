#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    # 1. PEP8: Use sys.argv to get the ID and ensure it exists
    if len(sys.argv) < 2:
        exit()

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # 2. Fetch User: Query specifically for the ID to avoid index errors
    # For ID 10, this fetches 'Clementina DuBuque' (exactly 18 characters)
    user_res = requests.get(url + "users/{}".format(employee_id))
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # 3. Fetch Todos: Get tasks belonging to this user
    todo_res = requests.get(url + "todos", params={"userId": employee_id})
    todo_data = todo_res.json()

    # 4. Filter: Get titles of tasks where completed is True
    completed_tasks = []
    for task in todo_data:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    # 5. Output: Exact format (Employee NAME is done with tasks(DONE/TOTAL):)
    # The first line must match character-for-character
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todo_data)))

    # 6. Formatting: One tab followed by one space and then the title
    for title in completed_tasks:
        print("\t {}".format(title))
