#!/usr/bin/python3
"""retrieve and display an employee's TODO list progress"""

import requests
import sys


def get_todo(employee_id):
    """gets the employees todo list"""
    # define the base url of the API
    base_url = "https://jsonplaceholder.typicode.com"
    # make an http request to get user data
    user_response = requests.get("{}/users/{}"
                                 .format(base_url, employee_id))
    # HTTPS error handling
    if user_response.status_code != 200:
        print("Error: Failed to get user data. Status code: {}"
              .format(user_response.status_code))
        sys.exit(1)
    # convert to JSON
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Invalid employee ID")
        return
    # make request to get todos data
    todos_response = requests.get("{}/users/{}/todos"
                                  .format(base_url, employee_id))
    if user_response.status_code != 200:
        print("Error: Failed to get user data. Status code: {}"
              .format(user_response.status_code))
        sys.exit(1)
    # convert
    todos_data = todos_response.json()
    # count number of completed and total tasks
    done_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    # print employee name and number of tasks and titles
    print("Employee {} is done with tasks({}/{}): "
          .format(user_data['name'], len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t", task["title"])


if __name__ == "__main__":
    # check if correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        # convert to integer
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    # calls function with given employee ID
    get_todo(employee_id)
