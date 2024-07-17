# from kivymd.app import MDApp
import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder 
from kivy.properties import ObjectProperty
# from backend import login_user
 
# Get the absolute path of the .kv file 
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'interface', 'auth', 'login.kv'))
Builder.load_file(kv_path)

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs) 
        self.successful = True

    def login(self):
        # username = self.username.text
        # password = self.password.text
        # response = login_user(username, password)
        # if response.get('detail') == 'Login successful':
        #     self.successful=True
        # else:
        #     print('Login failed: ', response.get('detail'))
        pass
