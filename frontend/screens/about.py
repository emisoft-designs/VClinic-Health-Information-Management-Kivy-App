#  clinic.py

import os
from kivymd.uix.screen import Screen 
from kivy.lang import Builder  
from backend import logout_user

# Get the absolute path of the .kv file
kv_path = os.path.join(os.path.dirname(__file__), '..', 'interface', 'about.kv')
kv_path = os.path.abspath(kv_path)  # Ensure it's an absolute path

Builder.load_file(kv_path)

class AboutScreen(Screen): 
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)  
        
    def logout(self):
        logout_user()
        