import json
from os import name
from pathlib import Path
import string
from prettytable import PrettyTable


def menu():
    print("========> This menu of app !")
    print('Enter your menu: >> a for add, e for edit, d for delete, l for list, s for status, c for exit')
    m = input()
    if m.__eq__("a"):
        print("========> Go to add new todo now !")
        add()
    elif m.__eq__("e"):
        print("========> Go to edit todo now !")
        edit()
    elif m.__eq__("d"):
        print("========> Go to delete todo now !")
        delete()
    elif m.__eq__("l"):
        print("========> Go to list todo now !")
        list()
    elif m.__eq__("s"):
        print("========> Go to status todo now !")
        status()
    elif m.__eq__("c"):
        print("========> exit now, good job !")
        exit()
    else:
        print("========> yeap, Type wrong !")
        menu()


def add():
    print("========> This add func of app :)")
    path = Path() / "todos.json"
    with open(path, mode="r", encoding="utf8") as jsonfile:
        todos = json.load(jsonfile)

    ids = []
    for todo in todos:
        ids.append(todo['id'])

    print('Please input new job name:')
    jobname = input()
    job = dict(id = max(ids) + 1, name = jobname, status = 0)
    todos.append(job)
    with open(path, mode="w", encoding="utf8") as jsonfile:
        json.dump(todos, jsonfile, indent=2)

    menu()

def edit():
    path = Path() / "todos.json"
    print("========> This edit func of app :)")
    print('Please input id number:')
    edit_id = input()
    print('Please input new job name:')
    edit_name = input()

    with open(path, mode="r", encoding="utf8") as jsonfile:
        todos = json.load(jsonfile)

    new_todos = []
    for todo in todos:
        if todo['id'] == int(edit_id):
            edit_job = dict(id = todo['id'], name = edit_name, status = todo['status'])
            new_todos.append(edit_job)
        else:
            new_todos.append(todo)

    with open(path, mode="w", encoding="utf8") as jsonfile:
        json.dump(new_todos, jsonfile, indent=2)
        print("edit ok!")

    menu()

def delete():
    print("========> This delete func of app :)")
    path = Path() / "todos.json"
    print('Please input id number:')
    delete_id = input()

    with open(path, mode="r", encoding="utf8") as jsonfile:
        todos = json.load(jsonfile)

    new_todos = []
    for todo in todos:
        if todo['id'] != int(delete_id):
            new_todos.append(todo)

    with open(path, mode="w", encoding="utf8") as jsonfile:
        json.dump(new_todos, jsonfile, indent=2)
        print("delete ok!")

    menu()

def list():
    path = Path() / "todos.json"
    print("========> This list func of app :)")

    print("jobs list:")
    
    t = PrettyTable(['Id', 'Name', "Status"])
    with open(path, "r") as jsonfile:
        todos = json.load(jsonfile)
        
        for todo in todos:
            t.add_row([todo["id"], todo['name'], convert_status(todo['status'])])

    print(t)

    menu()

def status():
    print("========> This status func of app :)")
    path = Path() / "todos.json"
    print('Please input id number:')
    edit_id = input()
    print('Please input new status (0 for New, 1 for Processing, 2 for Finished, other for Pending):')
    edit_status = input()

    with open(path, mode="r", encoding="utf8") as jsonfile:
        todos = json.load(jsonfile)

    new_todos = []
    for todo in todos:
        if todo['id'] == int(edit_id):
            edit_job = dict(id = todo['id'], name = todo['name'], status = int(edit_status))
            new_todos.append(edit_job)
        else:
            new_todos.append(todo)

    with open(path, mode="w", encoding="utf8") as jsonfile:
        json.dump(new_todos, jsonfile, indent=2)
        print("edit ok!")

    menu()

def convert_status(status: int) -> string:
    if status.__eq__(0):
        return "New"
    elif status.__eq__(1):
        return "Processing"
    elif status.__eq__(2):
        return "Finished"
    else:
        return "Pending"

menu()