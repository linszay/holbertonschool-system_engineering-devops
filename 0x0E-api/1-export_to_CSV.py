#!/usr/bin/python3
"""Exports data in the CSV format"""
import csv
import requests
import sys


def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}"
                                 .format(base_url, employee_id))
    user_data = user_response.json()

    if 'name' not in user_data:
        print("Invalid employee ID")
        return None, None

    todos_response = requests.get("{}/users/{}/todos"
                                  .format(base_url, employee_id))
    todos_data = todos_response.json()

    return user_data, todos_data


def export_to_csv(employee_id, user_data, todos_data):
    """exports data in the CSV format"""
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            csv_writer.writerow([employee_id, user_data["username"],
                                 task["completed"], task["title"]])

    print("Data exported to {}".format(file_name))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_data, todos_data = get_employee_data(employee_id)

    if user_data and todos_data:
        export_to_csv(employee_id, user_data, todos_data)
