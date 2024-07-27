#  clinic.py

import os
from kivymd.uix.screen import Screen 
from kivy.lang import Builder  
from backend import logout_user

# Get the absolute path of the .kv file
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'interface', 'contact.kv'))
Builder.load_file(kv_path)

class ContactScreen(Screen): 
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)  
        
    def logout(self):
        logout_user()