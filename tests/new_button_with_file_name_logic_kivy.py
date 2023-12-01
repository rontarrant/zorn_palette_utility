from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import ObjectProperty, StringProperty

class MyApplication(App):
	file_name = StringProperty(None)
	
	def build(self):
		# Create the main layout
		main_layout = BoxLayout(orientation = 'vertical')

		# Create widgets and add them to the main layout
		new_button = Button(text = 'New', on_press = self.on_new_button_clicked)
		main_layout.add_widget(new_button)

		# You can add more widgets as needed

		return main_layout

	def on_new_button_clicked(self, instance):
		# Implement the 'New' button functionality here
		popup_content = BoxLayout(orientation = 'vertical')
		popup_content.add_widget(Label(text = 'Do you want to save changes?'))

		save_button = Button(text = 'Save', on_press = self.save_data)
		cancel_button = Button(text = 'Cancel', on_press = self.cancel_save)

		popup_content.add_widget(save_button)
		popup_content.add_widget(cancel_button)

		self.popup = Popup(title = 'Save Changes', content = popup_content, size_hint = (0.5, 0.5))
		self.popup.open()

	def save_data(self, instance):
		# Implement save data logic
		self.popup.dismiss()
		
		if self.file_name:
			# Scenario 1: Use the existing file name
			self.save_data_to_file(self.file_name)
		else:
			# Scenario 2: Get a new file name from the user
			self.get_file_name_from_user()

	def cancel_save(self, instance):
		# Implement cancel save logic
		self.popup.dismiss()
		# Add your cancel save logic here
		print("Save operation canceled")

	def save_data_to_file(self, file_name):
		# Implement save data to file logic with the provided file name
		print(f"Data saved to file: {file_name}")

	def get_file_name_from_user(self):
		# Implement logic to get a new file name from the user
		# For simplicity, we use a TextInput in this example
		file_name_input = TextInput(text = '', multiline = False)
		popup_content = BoxLayout(orientation = 'vertical')
		popup_content.add_widget(Label(text = 'Enter a file name:'))
		popup_content.add_widget(file_name_input)

		save_button = Button(text = 'Save', on_press = lambda instance: self.save_data_with_new_file(file_name_input.text))
		cancel_button = Button(text = 'Cancel', on_press = self.cancel_save)

		popup_content.add_widget(save_button)
		popup_content.add_widget(cancel_button)

		new_file_popup = Popup(title = 'Enter File Name', content = popup_content, size_hint = (0.5, 0.5))
		new_file_popup.open()

	def save_data_with_new_file(self, new_file_name):
		# Implement save data to file logic with the new file name
		self.file_name = new_file_name
		print(f"Data saved to file: {new_file_name}")
		self.popup.dismiss()

if __name__ ==  '__main__':
	MyApplication().run()