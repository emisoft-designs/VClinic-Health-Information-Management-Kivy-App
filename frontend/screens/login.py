import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder 
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from backend import login_user

kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'interface', 'auth', 'login.kv'))
Builder.load_file(kv_path)


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None) 

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) 
        self.successful = False

    def login(self):
        username = self.username.text
        password = self.password.text
        print(f"username: {username}")
        response = login_user(username, password)
        
        if response:
            self.successful = True
            self.ids.login_info.text = "Login Successful"
            self.ids.login_info.color = (1, 1, 1, 1)  # White color for success messages
        else:
            self.successful = False
            self.ids.login_info.text = "Invalid Credentials"
            self.ids.login_info.color = (1, 0, 0, 1)  # Red color for error messages

    def on_pre_enter(self):
        self.successful = False 
        if hasattr(self.username, 'text'):
            self.username.text = ""
        if hasattr(self.password, 'text'):
            self.password.text = ""
