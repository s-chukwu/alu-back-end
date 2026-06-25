#!/usr/bin/python3
"""
Uses the REST API for a given employee ID to return
information about their TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get(
        "{}/users/{}".format(base, employee_id)
    ).json()

    todos = requests.get(
        "{}/todos?userId={}".format(base, employee_id)
    ).json()

    completed = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)
    ))

    [print("\t {}".format(title)) for title in completed]