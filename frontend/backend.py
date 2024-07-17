import requests

BASE_URL = 'http://127.0.0.1:8000/api/'

def login_user(username, password):
    url = BASE_URL + 'login/'
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()  # Returning user data
    return None

def logout_user():
    url = BASE_URL + 'logout/'
    response = requests.post(url=url)
    if response.status_code == 200:
        return response.json()  # Returning user data
    return None

def register_patient(data):
    url = BASE_URL + 'register_patient/'
    response = requests.post(url, data=data)
    return response.status_code == 201

def register_staff(data):
    url = BASE_URL + 'register_staff/'
    response = requests.post(url, data=data)
    return response.status_code == 201

def get_user_info(user_id):
    url = BASE_URL + f'users/{user_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None