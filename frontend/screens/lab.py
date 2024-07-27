# vclinic/frontend/screens/lab/lab.py

import os
from kivymd.uix.screen import Screen
from kivy.lang import Builder 
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import GridLayout
# from kivymd.uix.scrollview import ScrollView
# from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from backend import logout_user


dashboard_kv_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'interface','lab','dashboard.kv'))
list_kv_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'interface','lab' ,'records','lab_list.kv'))
details_kv_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'interface','lab' ,'records','lab_detail.kv'))
form_kv_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'interface','lab' ,'records','lab_form.kv'))

prenatal_kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                '..', 'interface','lab' ,'tests','prenatal.kv'))
gynae_preop_kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                   '..', 'interface','lab' ,'tests','gynae_preop.kv'))
csection_kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                '..', 'interface','lab' ,'tests','csection.kv'))
subfertility_kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                    '..', 'interface','lab' ,'tests','subfertility.kv'))
hiv_kv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                           '..', 'interface','lab' ,'tests','hiv.kv'))

Builder.load_file(dashboard_kv_path) 
Builder.load_file(list_kv_path) 
Builder.load_file(details_kv_path) 
Builder.load_file(form_kv_path)  

Builder.load_file(prenatal_kv_path) 
Builder.load_file(gynae_preop_kv_path) 
Builder.load_file(csection_kv_path) 
Builder.load_file(subfertility_kv_path)  
Builder.load_file(hiv_kv_path)  

class LaboratoryScreen(Screen):
    def __init__(self, **kwargs):
        super(LaboratoryScreen, self).__init__(**kwargs)
        self.add_widget(LabDashboardScreen(name='lab_dashboard'))  

class LabDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(LabDashboardScreen, self).__init__(**kwargs)

    def create_new_record(self, instance):
        print("New patient record created.")
        self.popup.dismiss()

    def pop_create_new_record(self):
        layout = GridLayout(cols=1)
        boxlayout = BoxLayout(padding=20, size_hint_y=None, height=60)
        gridlayout = GridLayout(cols=2, padding=10, size_hint_y=None, height=60)

        info_label = Label(padding=10, text="Do you wish to create a new patient's record?")
        createbtn = Button(text='Yes', size_hint_y=None, height=50)
        cancelbtn = Button(text='Cancel', size_hint_y=None, height=50)

        boxlayout.add_widget(info_label)
        gridlayout.add_widget(createbtn)
        gridlayout.add_widget(cancelbtn)

        layout.add_widget(boxlayout)
        layout.add_widget(gridlayout)

        self.popup = Popup(title="Create New Patient's Record", content=layout, 
                      size_hint=(None, None), size=(400,200), auto_dismiss=False)
        self.popup.open()

        createbtn.bind(on_press=self.create_new_record)
        cancelbtn.bind(on_press=self.popup.dismiss)

    def logout(self):
        logout_user()

    def search_other_tests(self):
        widget = TextInput(hint_text='Search for a test')
        popup = Popup(title='Search Tests', 
                      content=widget, 
                      size_hint=(None, None), 
                      size=(400, 300))
        popup.open()

    @property
    def recent_activities(self):
        # Placeholder for recent activities
        return ["Activity 1", "Activity 2", "Activity 3"]

    @property
    def notifications(self):
        # Placeholder for notifications
        return ["Notification 1", "Notification 2"]

# Generic Tests
class LabTestFormScreen(Screen):
    def __init__(self, **kwargs):
        super(LabTestFormScreen, self).__init__(**kwargs)
                                                
    def logout(self):
        logout_user()


class LabTestListScreen(Screen):
    def __init__(self, **kwargs):
        super(LabTestListScreen, self).__init__(**kwargs)
        self.layout = self.setup_record_ui() 
    
    def on_kv_post(self, base_widget):
        self.grid_layout = self.ids.record_table
        self.grid_layout.add_widget(self.layout)

    def logout(self):
        logout_user()
    
    def get_record_title(self):
        first_name  = "Jame"
        last_name = "Clement"
        return f"{first_name} {last_name} Test Records"
    
    def setup_record_ui(self):
        data_tables = MDDataTable(
            size_hint=(None, None),
            size=(850, 1200),
            pos_hint={"center_x":.5, "center_y":.5},
            padding=15,
            shadow_color=(0, 0.5, 0.7, 1),
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60)),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30)),
                ("Team Lead", dp(30))
            ],
            row_data=[
                ("1", ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                 "Astrid: NE shared managed", "Medium", "Triaged", "0:33",
                 "Chase Nguyen"),
                ("2", ("alert-circle", [1, 0, 0, 1], "Offline"),
                 "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
                 "Brie Furman"),
                ("3", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Phoenix: prod shared lyra-lists", "Minor",
                 "Not Triaged", "3:12", "Jeremy lake"),
                ("4", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Sirius: NW prod shared locations",
                 "Negligible",
                 "Triaged", "13:18", "Angelica Howards"),
                ("5", (
                    "checkbox-marked-circle",
                    [39 / 256, 174 / 256, 96 / 256, 1],
                    "Online"), "Sirius: prod independent account",
                 "Negligible",
                 "Triaged", "22:06", "Diane Okuma"),

            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2
        )
        data_tables.bind(on_row_press=self.on_row_press)
        data_tables.bind(on_check_press=self.on_check_press)
        return data_tables
    
    def update_row_data(self, *dt):
        self.data_tables.row_data = [
        (
            "21",
            ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
            "Astrid: NE shared managed",
            "Medium",
            "Triaged",
            "0:33",
            "Chase Nguyen"
        ),
        ("32", ("alert-circle", [1, 0, 0, 1], "Offline"),
        "Cosmo: prod shared ares", "Huge", "Triaged", "0:39",
        "Brie Furman"),
        ("43", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Phoenix: prod shared lyra-lists", "Minor",
        "Not Triaged", "3:12", "Jeremy lake"),
        ("54", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: NW prod shared locations",
        "Negligible",
        "Triaged", "13:18", "Angelica Howards"),
        ("85", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: prod independent account",
        "Negligible",
        "Triaged", "22:06", "Diane Okuma"),
        ("85", (
        "checkbox-marked-circle",
        [39 / 256, 174 / 256, 96 / 256, 1],
        "Online"), "Sirius: prod independent account",
        "Negligible",
        "Triaged", "22:06", "John Sakura"),
        ]


    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''
        self.changeScreen()
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)
    
    
    def changeScreen(self):
        if self.manager.current == 'lab_test_list':
            self.manager.current = 'lab_test_detail'
        else:
            self.manager.current = 'lab_test_list'

class LabTestDetailScreen(Screen):
    def __init__(self, **kwargs):
        super(LabTestDetailScreen, self).__init__(**kwargs)

    def get_record_title(self):
        first_name  = "Jame"
        last_name = "Clement"
        return f"{first_name} {last_name} Test Records"
        
    def logout(self):
        logout_user()

# Custom Tests
class SubfertilityTestForm(Screen):
    def __init__(self, **kwargs):
        super(SubfertilityTestForm, self).__init__(**kwargs)
        
    def logout(self):
        logout_user()

class PrenatalTestForm(Screen):
    def __init__(self, **kwargs):
        super(PrenatalTestForm, self).__init__(**kwargs)
        
    def logout(self):
        logout_user()

class GynaePreOpTestForm(Screen):
    def __init__(self, **kwargs):
        super(GynaePreOpTestForm, self).__init__(**kwargs)
        
    def logout(self):
        logout_user()

class CSectionTestForm(Screen):
    def __init__(self, **kwargs):
        super(CSectionTestForm, self).__init__(**kwargs)
        
    def logout(self):
        logout_user()

class HIVTestForm(Screen):
    def __init__(self, **kwargs):
        super(HIVTestForm, self).__init__(**kwargs)
        
    def logout(self):
        logout_user()




