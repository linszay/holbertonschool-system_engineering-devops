#!/usr/bin/python3
"""retrieve and display an employee's TODO list progress"""

import requests as req
import sys


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve employee information
    employee_id = sys.argv[1]
    user_response = req.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id))
    todo_response = req.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": employee_id})

    # Check for request errors
    if user_response.status_code != 200:
        print("Error: User ID not found")
        sys.exit(1)
    if todo_response.status_code != 200:
        print("Error: Could not retrieve TODO list")
        sys.exit(1)

    # Parse JSON responses
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extract relevant data
    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task["completed"])
    completed_titles = [task["title"]
                        for task in todo_data if task["completed"]]

    # Display TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          done_tasks, total_tasks))
    for title in completed_titles:
        print("\t {}".format(title))
