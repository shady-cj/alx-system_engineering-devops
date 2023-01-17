#!/usr/bin/python3
"""
Using python to consume apis that displays
a users todos and writes it to a csv
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys
    if len(sys.argv) < 2:
        sys.exit()
    id = sys.argv[1]
    if not id.isnumeric():
        sys.exit()
    filename = "{}.csv".format(id)
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    user = user.json()
    username = user.get("username")
    user_todos = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    for todo in todos:
        if todo.get("userId") == int(id):
            task_completed = todo.get("completed")
            title = todo.get("title")
            t = [id, username, task_completed, title]
            user_todos.append(t)

    with open(filename, "w", encoding="UTF-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(user_todos)
