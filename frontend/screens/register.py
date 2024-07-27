# register.py

import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder 


# Get the absolute path of the .kv file
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                       '..', 'interface','register','register.kv'))
Builder.load_file(kv_path)
 
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs) 
    pass