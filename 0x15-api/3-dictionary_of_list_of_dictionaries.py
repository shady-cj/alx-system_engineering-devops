#!/usr/bin/python3
"""
Using python to consume apis that displays
a users todos and writes it to a json file
"""

if __name__ == "__main__":
    import json
    import requests
    filename = "todo_all_employees.json"
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    obj = {}
    for user in users:
        username = user.get("username")
        id = user.get("id")
        obj[id] = []
        for todo in todos:
            if todo.get("userId") == id:
                task_completed = todo.get("completed")
                title = todo.get("title")
                t_info = {
                    "username": username,
                    "task": title,
                    "completed": task_completed
                }
                obj[id].append(t_info)

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False)
