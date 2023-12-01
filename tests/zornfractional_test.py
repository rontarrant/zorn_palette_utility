from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import ListProperty

kv = Builder.load_file("zornfractional_test.kv")

class MyLabel(Label):
	dynamic_colour = ListProperty([])


class ZornTestApp(App):
	def build(self):
		return MyLabel()

if __name__ == "__main__":
	ZornTestApp().run()
