from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MyApplication(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')

        # Create widgets and add them to the main layout
        new_button = Button(text='New', on_press=self.on_new_button_clicked)
        main_layout.add_widget(new_button)

        # You can add more widgets as needed

        return main_layout

    def on_new_button_clicked(self, instance):
        # Implement the 'New' button functionality here
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text='Do you want to save changes?'))

        save_button = Button(text='Save', on_press=self.save_data)
        cancel_button = Button(text='Cancel', on_press=self.cancel_save)

        popup_content.add_widget(save_button)
        popup_content.add_widget(cancel_button)

        self.popup = Popup(title='Save Changes', content=popup_content, size_hint=(0.5, 0.5))
        self.popup.open()

    def save_data(self, instance):
        # Implement save data logic
        self.popup.dismiss()
        # Add your save data logic here
        print("Data saved successfully")

    def cancel_save(self, instance):
        # Implement cancel save logic
        self.popup.dismiss()
        # Add your cancel save logic here
        print("Save operation canceled")

if __name__ == '__main__':
    MyApplication().run()