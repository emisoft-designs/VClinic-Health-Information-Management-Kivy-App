# main.py

import os
import sys 

from kivy.resources import resource_add_path, resource_find
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'minimum_width', '1100')
Config.set('graphics', 'minimum_height', '600')

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from screens.login import LoginScreen
from screens.home import HomeScreen
from screens.notifications import NotificationScreen
from screens.about import AboutScreen
from screens.services import ServiceScreen
from screens.contact import ContactScreen
from screens.register_patient import RegisterPatientScreen
from screens.lab import *
from screens.gynae import *
from screens.obstetrics import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
def get_image_dir(name):
    img_path = os.path.join(os.path.dirname(__file__), 'static', 'images', name)
    return img_path

class WindowManager(ScreenManager):
    pass 

class VClinic(MDApp):
    def build(self):
        kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'interface', 'main.kv'))
        self.icon = 'static\images\icon.png'  
        return Builder.load_file(kv_path)

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    VClinic().run()
