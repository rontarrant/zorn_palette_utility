## This doesn't work very well yet. Perhaps it never will.

## Zorn Colour Palette Mixer
## GridLayout 4x5
## Step 1: get RGB values of a subset of web-safe colours
## Step 2: Build a dictionary with these RGB values
## Step 3: Build a UI with:
##	- a drop-down list of the colours,
## - a 4x5 grid for mixing colours
## - an extra column to the left of the mixing grid with 
##   drop-down lists of colours in the first and last rows,
## - an extra row above the mixing grid with colour drop-downs in the
##   2nd and 4th columns
## - an extra cell above the extra column and to the left of the extra
##   row containing:
##		- a button for saving the palette (or an image of the mixing grid
##      with RGB values for all colours)
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
import kivy.metrics

## local
import web_safe_subset_rgb as colours

class ColourSpinner(Spinner):
	values = colours.WebColours
	#size_hint = (None, None)
	#size = (150, 150)
	
	def __init__(self, **kwargs):
		super(ColourSpinner, self).__init__(**kwargs)
		##self.bind(on_release = lambda instance: self.spinner_clicked(instance, self.text))
		self.bind(on_text = self.spinner_clicked(self.text))
		#self.text = "Pick a Colour"
		
	def spinner_clicked(self, text):
		self.text = text
		print("Colour selected: ", text)


class SpacerLabel(Label):
	text = ""
	#size_hint = (None, None)
	#width = 150
	#height = 150
	
	def __init__(self, **kwargs):
		super(SpacerLabel, self).__init__(**kwargs)


class SaveButton(Button):
	text = "Save"

	def __init__(self, **kwargs):
		super(SaveButton, self).__init__(**kwargs)
		self.text_size = self.size


class ZornGridLayout(GridLayout):
	row_force_default = True
	row_default_height = kivy.metrics.dp(150)
	minimum_height = kivy.metrics.dp(900)
	column_force_default = True
	column_default_height = kivy.metrics.dp(150)
	minimum_width = kivy.metrics.dp(750)
	padding = 5, 5, 5, 5
	rows = 6
	cols = 5
	
	def __init__(self, **kwargs):
		super(ZornGridLayout, self).__init__(**kwargs)
		self.save_button = SaveButton()
		self.add_widget(self.save_button)
		
		self.spacer_label1 = SpacerLabel()
		self.spacer_label1.text_size = self.spacer_label1.size
		self.add_widget(self.spacer_label1)
		
		self.colour_spinner1 = ColourSpinner()
		self.colour_spinner1.id = "colour1"
		self.add_widget(self.colour_spinner1)
		


class ZornInPythonApp(App):
	def build(self):
		Window.size = 750, 900
		zorn_layout = ZornGridLayout()
		Window.add_widget(zorn_layout)

if __name__ == "__main__":
	ZornInPythonApp().run()
