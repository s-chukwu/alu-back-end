#!/usr/bin/python3
import requests
import sys


def get_todo_progress(employee_id):
    """Fetches and prints the TODO list progress for a specific employee ID."""
    base_url = "https://typicode.com"

    # Define targets for user data and task list endpoints
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Request employee details
        user_response = requests.get(user_url)
        if user_response.status_code != 200:
            return
        employee_name = user_response.json().get("name")

        # Request complete todo list items
        todos_response = requests.get(todos_url)
        if todos_response.status_code != 200:
            return
        tasks = todos_response.json()

        # Calculate task completions
        total_tasks = len(tasks)
        completed_tasks = [task for task in tasks if task.get("completed")]
        number_of_done_tasks = len(completed_tasks)

        # Print summary line matching the required formatting string
        print(f"Employee {employee_name} is done with tasks"
              f"({number_of_done_tasks}/{total_tasks}):")

        # Print each completed title with 1 tab and 1 space layout
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException:
        return


if __name__ == "__main__":
    # Ensure parameter exists prior to processing execution logic
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            get_todo_progress(emp_id)
        except ValueError:
            pass
