from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.label import Label

class DataTable(BoxLayout):
    data = ListProperty([])  # List of dictionaries to hold the table data
    columns = ListProperty([])  # List of column headers

    def __init__(self, **kwargs):
        super(DataTable, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.current_page = 0
        self.rows_per_page = 10
        self.sort_order = {col: False for col in self.columns}  # Track sort order
        self.filtered_data = self.data.copy()  # Copy of the data for filtering

        # Create header with sorting buttons
        self.header = GridLayout(cols=len(self.columns), size_hint_y=None, height=30)
        self.add_widget(self.header)
        self.update_header()

        # Create body with scrollable table
        self.body = ScrollView(size_hint=(1, 1))
        self.grid = RecycleView()
        self.layout = RecycleGridLayout(cols=len(self.columns), default_size=(None, 30), size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.grid.add_widget(self.layout)
        self.body.add_widget(self.grid)
        self.add_widget(self.body)

        # Create pagination controls
        self.pagination = BoxLayout(size_hint_y=None, height=30)
        self.prev_button = Button(text='Previous', on_press=self.prev_page)
        self.next_button = Button(text='Next', on_press=self.next_page)
        self.pagination.add_widget(self.prev_button)
        self.pagination.add_widget(self.next_button)
        self.add_widget(self.pagination)

        # Create filter inputs
        self.filters = GridLayout(cols=len(self.columns), size_hint_y=None, height=30)
        self.filter_inputs = []
        for col in self.columns:
            filter_input = TextInput(hint_text=f'Filter {col}', multiline=False, on_text_validate=self.filter_data)
            self.filter_inputs.append(filter_input)
            self.filters.add_widget(filter_input)
        self.add_widget(self.filters)

        self.update_table()

    def update_header(self):
        self.header.clear_widgets()
        for col in self.columns:
            btn = Button(text=col, size_hint_y=None, height=30, on_press=lambda instance, c=col: self.sort_data(c))
            self.header.add_widget(btn)

    def update_table(self):
        start_index = self.current_page * self.rows_per_page
        end_index = start_index + self.rows_per_page
        page_data = self.filtered_data[start_index:end_index]
        table_data = [{'text': str(page_data[row][col])} for row in range(len(page_data)) for col in self.columns]
        self.grid.data = table_data
        self.grid.refresh_from_data()

    def next_page(self, instance):
        if (self.current_page + 1) * self.rows_per_page < len(self.filtered_data):
            self.current_page += 1
            self.update_table()

    def prev_page(self, instance):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()

    def sort_data(self, column):
        self.filtered_data.sort(key=lambda x: x[column], reverse=self.sort_order[column])
        self.sort_order[column] = not self.sort_order[column]
        self.update_table()

    def filter_data(self, instance):
        self.filtered_data = self.data.copy()
        for i, col in enumerate(self.columns):
            filter_text = self.filter_inputs[i].text
            if filter_text:
                self.filtered_data = [row for row in self.filtered_data if filter_text.lower() in str(row[col]).lower()]
        self.current_page = 0
        self.update_table()

# class DataTableApp(App):
#     def build(self):
#         table = DataTable(
#             columns=['Column 1', 'Column 2', 'Column 3'],
#             data=[
#                 {'Column 1': f'Row {i+1} Col 1', 'Column 2': f'Row {i+1} Col 2', 'Column 3': f'Row {i+1} Col 3'}
#                 for i in range(100)
#             ]
#         )
#         return table

# if __name__ == '__main__':
#     DataTableApp().run()
