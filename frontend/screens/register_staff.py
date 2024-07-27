# register_staff.py

import os
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from backend import register_staff, logout_user

# Get the absolute path of the .kv file
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                       '..', 'interface','register','register_staff.kv'))
Builder.load_file(kv_path)


class RegisterStaffScreen(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    position = ObjectProperty(None)

    def register_staff(self):
        data = {
            'username': self.username.text,
            'email': self.email.text,
            'password': self.password.text,
            'position': self.position.text,
        }
        response = register_staff(data)
        print(response)
        
    def logout(self):
        response = logout_user()
        if response.get('detail') == 'Logout Successful':
            print('You have been successfully logged out')
