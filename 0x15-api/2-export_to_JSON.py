#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    to_do = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userId), verify=False).json()
    username = user.get('username')
    tasks = []
    for task in to_do:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[userId] = tasks
    with open("{}.json".format(userId), mode='w') as jsonfile:
        json.dump(jsonobj, jsonfile)
