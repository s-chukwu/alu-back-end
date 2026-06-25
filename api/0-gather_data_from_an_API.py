#!/usr/bin/python3
"""
Uses the REST API for a given employee ID to return
information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, employee_id)).json()
    todos = requests.get(
        "{}/todos?userId={}".format(base, employee_id)
    ).json()

    done = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)
    ))

    for task in done:
        print("\t {}".format(task.get("title")))
