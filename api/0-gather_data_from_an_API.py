#!/usr/bin/python3
import requests
import sys


def get_todo_progress():
    """
    Fetches and displays the progress of a specific employee's tasks.
    """
    # Check if an argument is provided
    if len(sys.argv) < 2:
        return

    try:
        # The employee ID is the first argument
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get employee information
    user_url = "{}users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Extract employee name
    employee_name = user_data.get("name")

    # Get todo list for the employee
    todos_url = "{}todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks and count total tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Print the summary line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        number_of_done_tasks,
        total_tasks
    ))

    # Print the titles of completed tasks with required formatting
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    get_todo_progress()