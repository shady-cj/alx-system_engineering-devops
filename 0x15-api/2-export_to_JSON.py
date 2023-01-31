#!/usr/bin/python3
"""
Using python to consume apis that displays
a users todos and writes it to a json file
"""

if __name__ == "__main__":
    import json
    import requests
    import sys
    if len(sys.argv) < 2:
        sys.exit()
    id = sys.argv[1]
    if not id.isnumeric():
        sys.exit()
    filename = "{}.json".format(id)
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    user = user.json()
    username = user.get("username")
    user_todos = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    obj = {id: []}
    for todo in todos:
        if todo.get("userId") == int(id):
            task_completed = todo.get("completed")
            title = todo.get("title")
            t_info = {
                    "task": title,
                    "completed": task_completed,
                    "username": username
                }
            obj[id].append(t_info)

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False)
