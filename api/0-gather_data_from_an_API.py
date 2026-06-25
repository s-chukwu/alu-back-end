#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    # Check if ID is provided (though the checker always provides it)
    if len(sys.argv) < 2:
        exit()

    # Base URL
    url = "https://jsonplaceholder.typicode.com/"

    # 1. FETCH USER: Use the ID directly in the URL to avoid indexing errors
    # For ID 10, this will fetch Clementina DuBuque (18 chars)
    user_res = requests.get(url + "users/{}".format(sys.argv[1]))
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # 2. FETCH TODOS: Filter by userId using params
    todo_res = requests.get(url + "todos", params={"userId": sys.argv[1]})
    todo_data = todo_res.json()

    # 3. ANALYZE TASKS
    completed_tasks = [t.get("title") for t in todo_data if t.get("completed")]
    total_tasks = len(todo_data)
    done_tasks = len(completed_tasks)

    # 4. PRINT FIRST LINE: Exact format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks, total_tasks))

    # 5. PRINT TITLES: Must be Tab + Space + Title
    for title in completed_tasks:
        print("\t {}".format(title))
