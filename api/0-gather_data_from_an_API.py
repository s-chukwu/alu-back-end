#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    # The API URL
    url = "https://jsonplaceholder.typicode.com/"

    # Get user information - sys.argv[1] is the ID
    user_url = "{}users/{}".format(url, sys.argv[1])
    user_response = requests.get(user_url)
    # The .json() method turns the response into a dictionary
    user_data = user_response.json()

    # Extract the name string directly
    employee_name = user_data.get("name")

    # Get todos for the specific user
    todos_url = "{}todos".format(url)
    params = {"userId": sys.argv[1]}
    todos_response = requests.get(todos_url, params=params)
    todos_data = todos_response.json()

    # Filter completed tasks and get titles
    completed_tasks = []
    for task in todos_data:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    # Formatted output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        len(completed_tasks),
        len(todos_data)
    ))

    # Print tasks with 1 tab and 1 space
    for title in completed_tasks:
        print("\t {}".format(title))