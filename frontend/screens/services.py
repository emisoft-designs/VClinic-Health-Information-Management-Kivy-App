#  services.py

import os
from kivymd.uix.screen import Screen 
from kivy.lang import Builder  
# from backend import logout_user

# Get the absolute path of the .kv file
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                       '..', 'interface','services.kv'))
Builder.load_file(kv_path)

class ServiceScreen(Screen): 
    def __init__(self, **kwargs):
        super(ServiceScreen, self).__init__(**kwargs)  
        
    def logout(self):
        # response = logout_user()
        # if response.get('detail') == 'Logout Successful':
        #     print('You have been successfully logged out')
        pass
        