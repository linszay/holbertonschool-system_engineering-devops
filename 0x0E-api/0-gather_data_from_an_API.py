#!/usr/bin/python3
"""Retrieve and display an employee's TODO list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]

    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for todo in done_tasks:
        print("\t {} {}".format('\t', todo['title']))
