#!/usr/bin/python3
"""doc"""
import requests
import sys
import urllib


def get_employee_todo_progress(employee_id):
    """doc"""
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}"
                                 .format(base_url, employee_id))
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Invalid employee ID")
        return

    todos_response = requests.get("{}/users/{}/todos"
                                  .format(base_url, employee_id))
    todos_data = todos_response.json()

    done_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}): "
          .format(user_data['name'], len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t", task["title"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
