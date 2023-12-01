## Zorn Fractional Colour Palette Mixer
from icecream import install
install()
ic.configureOutput(includeContext = True)

## python libraries
import os

## kivy libraries
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import ObjectProperty, StringProperty

## layouts
kv_main = Builder.load_file("main_window.kv")
kv_file = Builder.load_file("file_dialogs.kv")
kv_info = Builder.load_file("information_dialogs.kv")
kv_or_not = Builder.load_file("yes_or_no_dialog.kv")

## local imports
from magic_palette_colorkit_fractional import ColourLookUp as clu
from colour_calculations_fractional import ColourCalculations
from csv_file import FileWorks

class ColourChip(Label):
	dynamic_colour = ListProperty([])

class ColourSpinner(Spinner):
	halign = "center"
	
	def set_spinner_chip(self, colour_name, label):
		base_colour_chip = clu[colour_name]

		## new_colour is set to the first element of the tuple
		new_colour = base_colour_chip[0]
		
		## assign it to the colour_01 chip
		label.dynamic_colour = new_colour

class Colour01Spinner(ColourSpinner):
	pass

class Colour02Spinner(ColourSpinner):
	pass

class Mix01Spinner(ColourSpinner):
	pass

class Mix02Spinner(ColourSpinner):
	pass

class ReloadButton(Button):
	pass

class QuitButton(Button):
	def clean_up(self):
		root = self.parent.parent

class NewButton(Button):
	pass

class LoadButton(Button):
	pass
					
class SaveButton(Button):
	pass

class SaveAsButton(Button):
	pass

class LoadDialog(FloatLayout):
	load_button = ObjectProperty(None)
	cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
	save_button = ObjectProperty(None)
	text_input = ObjectProperty(None)
	cancel_button = ObjectProperty(None)
	set_pathname = ObjectProperty(None)
	set_filename = ObjectProperty(None)

class NewYesOrNoDialog(FloatLayout):
	new_yes_no_func = ObjectProperty(None)
	dismiss_dialog = ObjectProperty(None)

class LoadYesOrNoDialog(FloatLayout):
	load_yes_no_func = ObjectProperty(None)
	dismiss_dialog = ObjectProperty(None)

class ZornGridLayout(GridLayout):
	path = StringProperty(None)
	filename = StringProperty(None)
	default_colours = ["Titanium White", "Titanium White", "Titanium White", "Titanium White"]
	calc_colours = None
	file_works = None
	saved_data = ListProperty(None)
	new = False
	load_in_progress = False

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.set_saved_data()

	def set_saved_data(self):
		spinner1 = self.ids.colour_01_spinner.text
		spinner2 = self.ids.colour_02_spinner.text
		spinner3 = self.ids.mix_01_spinner.text
		spinner4 = self.ids.mix_02_spinner.text
		self.saved_data = [spinner1, spinner2, spinner3, spinner4]
	
	## Because pop-up dialog windows are shown one at a time,
	## this will dismiss whichever one is showing.
	def dismiss_popup(self):
		print("dismiss_popup...")
		self._popup.dismiss()

	def on_new_reset(self):
		## reset spinner text to defaults
		self.set_spinners_text()
		
		## reset self.saved_data to default colours (all Titanium White)
		self.set_saved_data()
		
		## reset the palette chips
		self.calc_colours.set_colours(self.ids)
		
		## set self.filename to an empty string
		self.filename = ""

	def on_new_button_pressed(self):
		self.new = True
		
		if self.compare_saved_data() == True: ## YES the data has been saved
			self.on_new_reset()
		else: ## NO there's NO data to be saved
			## open yes_or_no_dialog
			content = NewYesOrNoDialog(new_yes_no_func = self.new_yes_no, dismiss_dialog = self.dismiss_popup)
			self._popup = Popup(title = "Save current palette?", content = content, size_hint = (0.8, 0.8))
			self._popup.open()

	def new_yes_no(self, reply):
		if reply == True: ## YES, we want to save the data.
			self.dismiss_popup()
			self.on_save_button_pressed()
		else: ## NO, we do NOT want to save the data.
			self.dismiss_popup()
			self.on_new_reset()

	def load_yes_no(self, reply):
		if reply == True: ## YES, we want to save the data.
			self.dismiss_popup()
			self.on_save_button_pressed()
		else: ## NO, we do NOT want to save the data.
			self.dismiss_popup() ## This should dismiss the LoadYesOrNoDialog
			content = LoadDialog(load_button = self.load_file_data, cancel = self.dismiss_popup)
			self._popup = Popup(title = "Load file", content = content, size_hint = (0.9, 0.9))
			self._popup.open()
			ic()

	def on_load_button_pressed(self):
		self.load_in_progress = True
		## see if there's unsaved data
		if self.compare_saved_data() == True: ## YES the data is SAVED
			## create and open the load dialog
			content = LoadDialog(load_button = self.load_file_data, cancel = self.dismiss_popup)
			self._popup = Popup(title = "Load file", content = content, size_hint = (0.9, 0.9))
			self._popup.open()
		else:
			## NO, the data is NOT SAVED
			## build a yes/no dialog to see if the user wants to save the data
			content = LoadYesOrNoDialog(load_yes_no_func = self.load_yes_no, dismiss_dialog = self.dismiss_popup)
			self._popup = Popup(title = "Save current palette?", content = content, size_hint = (0.8, 0.8))
			self._popup.open()

	def load_file_data(self, path, filename):
		self.set_filename(filename[0])
		self.set_path(path)

		if self.filename: ## We need a file name to load
			colours = self.file_works.load_csv(self.path + "/" + self.filename)
			
			## check here to see if it's a good file
			if self.check_file_contents(colours):
				self.ids.colour_01_spinner.text = colours[0]
				self.ids.colour_02_spinner.text = colours[1]
				self.ids.mix_01_spinner.text = colours[2]
				self.ids.mix_02_spinner.text = colours[3]

				self.calc_colours.set_colours(self.ids)
				self.saved_data = colours
					
		self.dismiss_popup()
		self.load_in_progress = False

	def on_reload_button_pressed(self):
		if self.compare_saved_data() == False:
			self.set_spinners_text()
			self.calc_colours.set_colours(self.ids)
		
	## Make sure the file selected in the LoadFile dialog is
	## propertly formated before trying to open it.
	def check_file_contents(self, colours):
		global clu
		
		## assume the file is bad
		good_flag = False
		## if all these criteria are met, it's a good file
		## is the file empty?
		if colours != "":
			## does the file contain a list[]?
			## is the list exactly 4 elements long?
			if len(colours) == 4:
				## make sure each element matches a colour name string found in clu
				for colour in colours:
					if colour not in clu:
						good_flag = False
					else:
						good_flag = True

		return good_flag

	## This is set to set_path in show_save_dialog() when the SaveDialog is instantiated
	def set_path(self, path):
		self.path = path
	
	## This is set to set_filename in show_save() when the SaveDialog is instantiated
	def set_filename(self, filename):
		print("set_file_name...")
		
		## split the full path into separate file and path strings
		path_and_file = os.path.split(filename)

		self.filename = path_and_file[1]

	## This is called from main_window.kv -> SaveAsButton.on_release
	def on_save_as_button_pressed(self):
		self.show_save_dialog()
	
	def on_save_button_pressed(self):
		data = self.get_spinners_text()
		
		if data == ['Colour 1', 'Colour 2', 'Tint 1', 'Tint 2'] or \
			data == [] or \
			data == ["Titanium White", "Titanium White", "Titanium White", "Titanium White"]:
			## pop up an information dialog saying there's nothing to save.
			ic("Nothing to save...")
		elif self.filename == "" or self.filename == None:
			self.show_save_dialog()
		else:
			self.save()
		
	def show_save_dialog(self):
		content = SaveDialog()
		content.save_button = self.save
		content.cancel_button = self.dismiss_popup
		content.set_pathname = self.set_path
		content.set_filename = self.set_filename
		
		## This puts the currently-saved file name (if one exists)
		## in the Save Dialog we're about to open.
		if self.filename != "" and self.filename != None:
			content.text_input.text = self.filename
		
		if self.filename != None:
			content.filename = str(self.filename)
		
		if self.path:
			content.path = self.path
		
		if self.filename:
			content.text_input = self.filename
		
		self._popup = Popup(title = "Save file", content = content, size_hint = (0.9, 0.9))
		self._popup.open()
		
	def save(self):
		print("save...")
		data = []

		self.file_works.save_csv(self.path + "/" + self.filename, data)
		self.saved_data = self.get_spinners_text()
			
		if self.new == True:
			self.on_new_reset()
		
		if self.load_in_progress == True:
			content = LoadDialog(load_button = self.load_file_data, cancel = self.dismiss_popup)
			self._popup = Popup(title = "Load file", content = content, size_hint = (0.9, 0.9))
			self._popup.open()
			self.load_in_progress = False

	def calculate_colours(self):
		self.calc_colours.set_colours(self.ids)

	def compare_saved_data(self):
		current_colours = self.get_spinners_text()
		matched = BooleanProperty
		
		if current_colours == self.saved_data:
			matched = True
		else:
			matched = False

		return matched

	def set_spinners_text(self):
		if self.new == True:
			colours = self.default_colours
			self.saved_data = colours
			self.new = False
		else:
			colours = self.saved_data
		
		self.ids.colour_01_spinner.text = colours[0]
		self.ids.colour_02_spinner.text = colours[1]
		self.ids.mix_01_spinner.text = colours[2]
		self.ids.mix_02_spinner.text = colours[3]
		
	def get_spinners_text(self):
		## colour names from Spinner text
		spinner_01 = self.ids.colour_01_spinner.text
		spinner_02 = self.ids.colour_02_spinner.text
		spinner_03 = self.ids.mix_01_spinner.text
		spinner_04 = self.ids.mix_02_spinner.text
		data = [spinner_01, spinner_02, spinner_03, spinner_04]
		
		return data

class ZornFractionalApp(App):
	zorn_grid_layout = None
	
	def build(self):
		self.zorn_grid_layout = ZornGridLayout()
		self.zorn_grid_layout.calc_colours = ColourCalculations()
		self.zorn_grid_layout.file_works = FileWorks()
		Window.add_widget(self.zorn_grid_layout)
		Window.size = 600, 700
		Window.bind(on_request_close = self.exit_check)

	def exit_check(self, window = Window):
		## make sure the current palette is saved OR to be abandoned
		Window.close()
		## NOTE: Can the window's close button be intercepted?
		## - ask user if unsaved data should be saved
		##   and if so, call SaveButton.save_palette()
		## - kill app

if __name__ == "__main__":
	ZornFractionalApp().run()
