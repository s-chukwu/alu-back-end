#!/usr/bin/python3
"""
Script to get and display TODO list progress for an employee
using a REST APIs

"""

import requests
import sys


def fetch_todo_progress(employee_id: int):
    """ Fetches and displays TODO list progress for an employee
    indicated by the given ID.

    Args:
    - employee_id (int): ID of the employee to retrieve TODO list for.

    Returns:
    - None
    """
    # define core url patterns
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_info_url = f'{base_url}users/{employee_id}'
    todo_info_url = f'{base_url}todos?userId={employee_id}'

    # fetch user information
    user_response = requests.get(user_info_url)
    user_info = user_response.json()
    user_name = user_info.get('name')

    # fetch todo info and calculate totals
    todo_info = requests.get(todo_info_url)
    todo_response = todo_info.json()
    total_todos = len(todo_response)
    completed_todos = sum(todo.get("completed", False)
                          for todo in todo_response)

    # define output
    print(f"Employee {user_name} is done with\
        tasks({completed_todos}/{total_todos}):")

    for todo in todo_response:
        if todo.get('completed', False):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    # Checks if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Calling the function to get and display TODO list progress
    fetch_todo_progress(employee_id)
