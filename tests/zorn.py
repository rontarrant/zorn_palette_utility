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
from kivy.uix.button import Button

## local
from web_safe_subset_rgb import WebColours
from colour_calculations import ColourCalculations

class Colour01Spinner(Spinner):
	def set_spinner_chip(self, colour_name, label):
		print(f"Colour 01 is {self.text}")
		## look up new colour in dictionary
		new_colour = WebColours[colour_name]
		## assign it to the chip
		label.dynamic_colour = new_colour
		print(f"Colour 01: {label.dynamic_colour}")
		

class Colour02Spinner(Spinner):
	def set_spinner_chip(self, colour_name, label):
		print(f"Colour 02 is {self.text}")
		## look up new colour in dictionary
		new_colour = WebColours[colour_name]
		## assign it to the chip
		label.dynamic_colour = new_colour
		print(f"Colour 02: {label.dynamic_colour}")

class Tint01Spinner(Spinner):
	def set_spinner_chip(self, colour_name, label):
		print(f"Tint 01 is {self.text}")
		## look up new colour in dictionary
		new_colour = WebColours[colour_name]
		## assign it to the chip
		label.dynamic_colour = new_colour
		print(f"Tint 01: {label.dynamic_colour}")

class Tint02Spinner(Spinner):
	def set_spinner_chip(self, colour_name, label):
		print(f"Tint 02 is {self.text}")
		## look up new colour in dictionary
		new_colour = WebColours[colour_name]
		## assign it to the chip
		label.dynamic_colour = new_colour
		print(f"Tint 02: {label.dynamic_colour}")

class NewButton(Button):
	def create_new(self):
		print("creating new")
		
class SaveButton(Button):
	def save_palette(self):
		print("saving palette")

class LoadButton(Button):
	def load_palette(self):
		print("loading palette")

class ZornGridLayout(GridLayout):
	def __init__(self, **kwargs):
		super(ZornGridLayout, self).__init__(**kwargs)
		self.calc_colours = ColourCalculations()
		
	def calculate_colours(self):
		self.calc_colours.set_colours(self.ids)


class ZornApp(App):
	def build(self):
		Window.size = 750, 900
		return ZornGridLayout()
	
if __name__ == "__main__":
	ZornApp().run()
