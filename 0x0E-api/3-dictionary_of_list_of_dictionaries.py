#!/usr/bin/python3
"""Export data in the JSON format for all employees"""

import json
import requests


def export_all_to_json():
    """Exports data to JSON file for all employees"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_resp = requests.get("{}/users".format(base_url))
    users = user_resp.json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        user_name = user['username']

        todo_resp = requests.get("{}/users/{}/todos".format(base_url, user_id))
        todos = todo_resp.json()

        tasks = []
        for todo in todos:
            task = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user_name
            }
            tasks.append(task)

        all_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_to_json()
