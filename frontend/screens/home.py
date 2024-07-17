import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
# from kivy.core.window import Window
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
from widgets.widgets import AnimatedButton
# from backend import logout_user

# Get the absolute path of the .kv file 
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'interface', 'home.kv'))
Builder.load_file(kv_path)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.menu_open = False

    def logout(self):
        # response = logout_user()
        # if response.get('detail') == 'Logout Successful':
        #     print('You have been successfully logged out')
        pass
        
