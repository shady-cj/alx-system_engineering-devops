#!/usr/bin/python3
"""
Using python to consume apis and display
informations
"""

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2:
        sys.exit()
    id = sys.argv[1]
    if not id.isnumeric():
        sys.exit()
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user.json()
    user_name = user.get("name")
    user_todos = {"completed": 0, "todos": 0, "todos_complete": []}
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    for todo in todos:
        if todo.get("userId") == int(id):
            if todo.get("completed"):
                user_todos["completed"] += 1
                user_todos["todos_complete"].append(todo)
            user_todos["todos"] += 1
    print(f"Employee {user_name} is done with \
tasks({user_todos['completed']}/{user_todos['todos']}):")
    for t in user_todos["todos_complete"]:
        print(f"\t {t.get('title')}")
