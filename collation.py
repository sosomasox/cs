#!/usr/bin/env python3

import ast
import datetime
import json
import pprint
import requests

ADL_URL  = 'http://localhost:3001/api/v1/activities/'
TODO_URL = 'http://localhost:3002/api/v1/todo/'

date_str = str(datetime.date.today())

res = requests.get(TODO_URL + 'date/' + date_str)
todo_data = json.loads(res.text)[0]

print("予定データ:")
pprint.pprint(todo_data)
print()

activity_str = todo_data['content']

res = requests.get(ADL_URL + activity_str + '/date/' + date_str)
adl_data = json.loads(res.text)[0]

print("行動データ:")
pprint.pprint(adl_data)
print()

if adl_data['count']:
    print("照合成功")
    print()

    _id = todo_data['_id']
    update_todo_data = todo_data
    update_todo_data['done'] = "true"
    update_todo_data.pop('_id')
    update_todo_data.pop('createdAt')
    update_todo_data.pop('updatedAt')

    res = requests.put(TODO_URL + 'id/' + _id, update_todo_data)
    ret = json.loads(res.text)
    
    print("更新後の予定データ:")
    pprint.pprint(ret)
    print()

else:
    print("照合失敗")
    print()
