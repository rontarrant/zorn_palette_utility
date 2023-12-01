from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

kv_string = '''
<MyLayout>:
    FileChooserListView:
        id: file_chooser
        path: root.initial_directory
        selection: root.file_name if root.file_name else []
'''

class MyLayout(BoxLayout):
    initial_directory = '/path/to/your/directory'
    file_name = StringProperty(None)

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.bind(file_name=self.update_selection)

    def update_selection(self, instance, value):
        if self.ids.file_chooser:
            self.ids.file_chooser.selection = [value] if value else []

class YourApp:
    def run(self):
        Builder.load_string(kv_string)
        self.root = MyLayout()

YourApp().run()