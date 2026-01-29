#Выделенный файл для работы с файлами

import pathlib
import os
import json

base_path = str(pathlib.Path(__file__).parent.resolve())[:-10]
SESSION_PATH = f'{base_path}/sessions'
#Осторожно, костыль. [:-10] возвращает корневую папку всего проекта, несмотря на то, что этот файл лежит в папке subscript
#Возможно есть решение покрасивее. Но это тоже работает.

def return_image(path, placeholder):
    full_path = f"{base_path}/static/images/{path}.jpg"
    if os.path.exists(full_path):
        return f'images/{path}.jpg'
    else:
        return f'images/common/{placeholder}.jpg'

def commonkwargs(email):
    if (getuser(email) != False):
        user = getuser(email)
        ans = dict()
        ans['userimg'] = return_image(f'users/{email}', 'user_placeholder')
        for u in user:
            if (u != 'password'):
                ans[u] = user[u]
        return ans
    else:
        return {'username': 'Log in', 'userimg': return_image(f'users/{email}', 'user_placeholder'), \
            'description': 'empty', 'phone': 'N/A', 'rights': 0, 'money': 0}

def getuser(email):
    users_path = f"{base_path}/users/{email}.json"
    if os.path.exists(users_path):
        with open(users_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    return False

def setuser(email, changes):
    users_path = f"{base_path}/users/{email}.json"
    with open(users_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(changes, indent = 4))

def settovar(id, to):
    tovars = gettovarlist()
    tovars[str(id)] = to
    users_path = f"{base_path}/tovars/tovars.json"
    with open(users_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(tovars, indent = 4))

def gettovar(id):
    tovars_path = f"{base_path}/tovars/tovars.json"
    with open(tovars_path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())[id]
    if os.path.exists(tovars_path):
        with open(tovars_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    return False

def setglobtovar(id, to):
    tovars = gettovarlist()
    tovars[str(id)] = to
    users_path = f"{base_path}/tovars/globtovars.json"
    with open(users_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(tovars, indent = 4))

def getglobtovar(id):
    tovars_path = f"{base_path}/tovars/globtovars.json"
    with open(tovars_path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())[id]
    if os.path.exists(tovars_path):
        with open(tovars_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    return False

def setquerylist(name, to):
    users_path = f"{base_path}/queries/{name}"
    with open(users_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(to, indent = 4))

def getquerylist(name):
    tovars_path = f"{base_path}/queries/{name}"
    if os.path.exists(tovars_path):
        with open(tovars_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    return False

def gettovarlist():
    with open(f"{base_path}/tovars/tovars.json", 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def getglobtovarlist():
    with open(f"{base_path}/tovars/global_tovars.json", 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def getcats():
    with open(f"{base_path}/tovars/list_of_categories.json", 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def setcats(to):
    with open(f"{base_path}/tovars/list_of_categories.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(to, indent = 4))

def setglobtovarlist(to):
    #users_path = f"{base_path}/tovars/global_tovars.json" #########################################
    users_path = f"{base_path}/tovars/tovars.json"
    with open(users_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(to, indent = 4))

def parse_menu_txt():
    jason = {}
    cats = {}
    last = "hohoho"
    with open(f'{base_path}/tovars/global_menu.txt', 'r', encoding='utf-8') as f:
        arr = f.read().split('\n')
        i = 6
        id = 1
        while (i < len(arr) - 1):
            if (arr[i + 3][-1] != '₽'):
                last = arr[i]
                i += 1
            jason[id] = ({"name": arr[i], "category": last, "price": int(arr[i + 3][0:-1]), \
                        "weight": int(arr[i + 2][0:-3]), "description": arr[i + 1], "badge": "ниче", \
                        "old_price": 0, "badge": "гойда", "main_icon": "bi-cup-straw", \
                        "specs": {"Калорийность": "45 ккал", "Сарах": "5 г", "Объём": "200 мл", "Температура": "Холодный"},
                        "reviews": [], "gallery": ["bi-cup-straw"]})
            cats |= {last: 1}
            i += 4
            id += 1
    return [jason, cats]