#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
"""
import sys
import requests

# Check if an argument (employee ID) has been provided
if len(sys.argv) < 2:
    print("Please provide an employee ID as an argument.")
    sys.exit()

employee_id = int(sys.argv[1])

# Make a GET request to the API to retrieve the employee's information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee = response.json()

# Make a GET request to the API to retrieve the employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
todo_list = response.json()

# Count the number of completed and non-completed tasks
num_completed_tasks = 0
total_num_tasks = len(todo_list)

for task in todo_list:
    if task["completed"]:
        num_completed_tasks += 1

# Print the employee's TODO list progress
print(f"Employee {employee['name']} is done with tasks({num_completed_tasks}/{total_num_tasks}):")

# Print the titles of completed tasks, with a tabulation and a space before each title
for task in todo_list:
    if task["completed"]:
        print(f"\t {task['title']}")
