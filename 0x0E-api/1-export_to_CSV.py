#!/usr/bin/python3
"""extending script to export data in CSV format"""
import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def get_username(id):
    """ Fetch user name """

    resp = requests.get(users_url).json()

    name = None
    for i in resp:
        if i['id'] == id:
            name = i['username']
            break

    return name


def export_to_csv(user_id):
    """ Export user's tasks to CSV """

    user_tasks = []
    resp = requests.get(todos_url).json()

    for i in resp:
        if i['userId'] == user_id:
            user_tasks.append([user_id, get_username(
                user_id), str(i['completed']), i['title']])

    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for row in user_tasks:
            writer.writerow(row)

    print(f"Exported {len(user_tasks)} tasks to {filename}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    export_to_csv(user_id)
