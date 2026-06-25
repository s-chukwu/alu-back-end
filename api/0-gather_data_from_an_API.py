#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress.
Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for a given employee."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_data = requests.get(user_url).json()
    employee_name = user_data.get("name")

    todos_url = "{}/todos".format(base_url)
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)