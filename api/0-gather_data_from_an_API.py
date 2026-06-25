#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # 1. Fetch user data
    # sys.argv[1] is the employee ID passed as an argument
    user_res = requests.get(url + "users/{}".format(sys.argv[1]))
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # 2. Fetch todo data
    todo_res = requests.get(url + "todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()

    # 3. Process tasks
    completed_tasks = [t.get("title") for t in todo_data if t.get("completed")]
    total_tasks = len(todo_data)
    done_tasks = len(completed_tasks)

    # 4. Print Summary (Format: Employee NAME is done with tasks(DONE/TOTAL):)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # 5. Print Titles (Format: Tab + Space + Title)
    for title in completed_tasks:
        print("\t {}".format(title))
