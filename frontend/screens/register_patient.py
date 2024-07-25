# register_patient.py

import os
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from backend import logout_user

from backend import register_patient

# Get the absolute path of the .kv file
kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                       '..', 'interface','register','register_patient.kv'))
Builder.load_file(kv_path)

class RegisterPatientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    firstname = ObjectProperty(None)
    middlename = ObjectProperty(None)
    surname = ObjectProperty(None)
    occupation = ObjectProperty(None)
    house_number = ObjectProperty(None)
    street = ObjectProperty(None)
    landmark = ObjectProperty(None)
    city = ObjectProperty(None)
    state = ObjectProperty(None)
    country = ObjectProperty(None)
    phone_number = ObjectProperty(None)
    marital_status = ObjectProperty(None)
    next_of_kin_firstname = ObjectProperty(None)
    next_of_kin_surname = ObjectProperty(None)
    next_of_kin_phone_number = ObjectProperty(None)
    next_of_kin_address_1= ObjectProperty(None)
    age = ObjectProperty(None)
    weight = ObjectProperty(None)
    height = ObjectProperty(None)
    additional_details = ObjectProperty(None)

    def register_patient(self):
        data = {
            'firstname': self.name.text,
            'middlename': self.name.text,
            'surname': self.name.text,
            'occupation': self.occupation.text,
            'address': self.address.text,
            'phone_number': self.phone_number.text,
            'marital_status': self.marital_status.text,
            'next_of_kin': self.next_of_kin.text,
            'weight': self.weight.text,
            'height': self.height.text,
            'additional_details': self.additional_details.text,
        }
        response = register_patient(data)
        print(response)
        
    def logout(self):
        # response = logout_user()
        # if response.get('detail') == 'Logout Successful':
        #     print('You have been successfully logged out')
        pass