#!/usr/bin/python3
"""Export an employee's tasks in JSON format"""

import json
import requests
from sys import argv, exit


def export_employee_tasks_to_json(employee_id):
    """Export an employee's tasks to a JSON file"""
    baseurl = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get("{}/users/{}".format(baseurl, employee_id))
    userdata = user_resp.json()

    if 'id' not in userdata or userdata['id'] != employee_id:
        print("Invalid employee ID")
        return

    todo_resp = requests.get("{}/users/{}/todos".format(baseurl, employee_id))
    tododata = todo_resp.json()

    employee_tasks = {str(employee_id): []}

    for task in tododata:
        employee_tasks[str(employee_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": userdata["username"]
        })

    if not isinstance(employee_tasks[str(employee_id)], list) or not all:
        with open(f"{employee_id}.json", "w") as f:
            json.dump(employee_tasks, f)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    export_employee_tasks_to_json(employee_id)
