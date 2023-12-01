from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import BooleanProperty

class MyObject():
	my_var = BooleanProperty()

	def on_my_var(self):
		self.my_var = True
		print(self.my_var)

class MyOtherObject():
	my_object = MyObject()
	
	def some_method(self):
		self.my_object.on_my_var()

my_other_object = MyOtherObject()
my_other_object.some_method()
