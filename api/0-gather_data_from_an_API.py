#!/usr/bin/python3
"""Retrieve and display an employee's completed TODO tasks."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com"

    employee = requests.get(
        "{}/users/{}".format(api_url, employee_id)
    ).json()

    tasks = requests.get(
        "{}/todos".format(api_url),
        params={"userId": employee_id}
    ).json()

    completed_tasks = [
        task for task in tasks if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"),
            len(completed_tasks),
            len(tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
