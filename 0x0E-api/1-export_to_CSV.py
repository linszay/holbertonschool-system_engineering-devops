#!/usr/bin/python3
"""extending script to export data in CSV format"""
import requests
import sys
import csv


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in todos:
            completed_status = "True" if todo["completed"] else "False"
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': completed_status,
                'TASK_TITLE': todo["title"]
            })
