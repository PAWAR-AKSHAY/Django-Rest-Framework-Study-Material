import requests
import json

URL = 'http://127.0.0.1:8000/student/'


def get_data(id=None):
    student_data = {}
    if id is not None:
        student_data = {'id': id}
    json_data = json.dumps(student_data)
    headers = {'content-Type': 'application/json'}

    response = requests.get(url=URL, data=json_data, headers=headers)
    data = response.json()
    print(data)


# get_data(1)


def post_data():
    student_data = {
        'name': 'Shivnath Shinde',
        'roll': 104,
        'city': 'Pune'
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(student_data)
    response = requests.post(url=URL, data=json_data, headers=headers)
    data = response.json()
    print(data)


# post_data()


def update_data():
    student_data = {
        'id': 4,
        'city': 'Mumbai'
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(student_data)
    response = requests.put(url=URL, data=json_data, headers=headers)
    data = response.json()
    print(data)


# update_data()


def delete_data():
    student_data = {
        'id': 4
    }
    json_data = json.dumps(student_data)
    headers = {'content-Type': 'application/json'}

    response = requests.delete(url=URL, data=json_data, headers=headers)
    data = response.json()
    print(data)


delete_data()
