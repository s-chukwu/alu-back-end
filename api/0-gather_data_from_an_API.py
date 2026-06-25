#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the ID provided as an argument
    employee_id = sys.argv[1]
    user_res = requests.get(url + "users/{}".format(employee_id))
    user_data = user_res.json()

    # Get the employee name
    employee_name = user_data.get("name")

    # Get the TODO list for the employee
    todo_res = requests.get(url + "todos", params={"userId": employee_id})
    todo_data = todo_res.json()

    # Filter tasks that are completed
    completed_tasks = []
    for task in todo_data:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    # Calculate total number of tasks
    total_tasks = len(todo_data)
    done_tasks = len(completed_tasks)

    # Print the first line in the required format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # Print each completed task title with one tab and one space
    for title in completed_tasks:
        print("\t {}".format(title))