import requests
import json

URL = 'http://127.0.0.1:8000/student/'


def get_data(id=None):
    student_data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(student_data)

    response = requests.get(url=URL, data=json_data)
    data = response.json()
    print(data)


# get_data()


def post_data():
    student_data = {
        'name': 'rakshay',
        'roll': 124,
        'city': 'Mumbai'
    }

    json_data = json.dumps(student_data)
    response = requests.post(url=URL, data=json_data)
    data = response.json()
    print(data)


post_data()


def update_data():
    student_data = {
        'id': 3,
        'name': 'Lucky waLLer',
        'city': 'Pune'
    }
    json_data = json.dumps(student_data)
    response = requests.put(url=URL, data=json_data)
    data = response.json()
    print(data)


# update_data()


def delete_data():
    student_data = {
        'id': 4
    }
    json_data = json.dumps(student_data)
    response = requests.delete(url=URL, data=json_data)
    data = response.json()
    print(data)


# delete_data()
