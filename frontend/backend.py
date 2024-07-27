import requests

BASE_URL = 'http://127.0.0.1:8000/api/'
auth_token = None

def set_auth_token(token):
    global auth_token
    auth_token = token

def get_headers():
    headers = {'Content-Type': 'application/json'}
    if auth_token:
        headers['Authorization'] = f'Token {auth_token}'
    return headers

def login_user(username, password):
    url = BASE_URL + 'login/' 
    data = {'username': username, 'password': password} 
    response = requests.post(url, json=data, headers=get_headers())
    if response.status_code == 200:
        token = response.json().get('token') 
        set_auth_token(token)
        return response
    
def logout_user():
    url = BASE_URL + 'logout/' 
    response = requests.post(url, headers=get_headers())
    if response.status_code == 200: 
        set_auth_token(None) 
        return response
    
def register_patient(data):
    url = BASE_URL + 'patients/register/'
    response = requests.post(url, json=data, headers=get_headers())
    return response.status_code == 201

def register_staff(data):
    url = BASE_URL + 'staff/register/'
    response = requests.post(url, json=data, headers=get_headers())
    return response.status_code == 201

def get_user_info(user_id):
    url = BASE_URL + f'users/{user_id}/'
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return None
