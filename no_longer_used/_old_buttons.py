
class LoadButton(Button):
	def load(self, path, filename):
		root = self.parent.parent
		ic()
		if root.compare_saved_data() == True:
			root.filename = filedialog.askopenfilename(filetypes = [("Comma-separated Values", "*.csv")])
			
			if root.filename:
				colours = root.file_works.load_csv(root.filename)
				ic(colours)
				## check here to see if it's a good file
				if self.check_file_contents(colours):
					ic()
					root.ids.colour_01_spinner.text = colours[0]
					root.ids.colour_02_spinner.text = colours[1]
					root.ids.mix_01_spinner.text = colours[2]
					root.ids.mix_02_spinner.text = colours[3]

					root.calc_colours.set_colours(root.ids, root)
					root.saved_data = colours
		ic(root.saved_data)

	def check_file_contents(self, colours):
		global clu
		
		## assume the file is bad
		good_flag = False
		ic(colours, good_flag)
		## if all these criteria are met, it's a good file
		## is the file empty?
		if colours != "":
			ic("colours is NOT empty")
			## does the file contain a list[]?
			## is the list exactly 4 elements long?
			if len(colours) == 4:
				ic("colours has 4 elements")
				## make sure each element matches a colour name string found in clu
				for colour in colours:
					ic(colour)
					if colour not in clu:
						good_flag = False
					else:
						good_flag = True
						ic(good_flag)
						ic(good_flag)
		ic(good_flag)
		return good_flag
					
		
class SaveButton(Button):
	def save_palette(self):
		root = self.parent.parent
		ids = root.ids
		data = None
		ic()

		if root.filename:
			data = root.get_spinners_text()
			ic(data)
			root.file_works.save_csv(root.filename, data)
			root.saved_data = data
		else:
			root.filename = filedialog.asksaveasfilename(filetypes = [("Comma-separated Values", "*.csv")])
			
			if root.filename:
				data = root.get_spinners_text()
				ic(data)
				root.file_works.save_csv(root.filename, data)
				root.saved_data = data
			else:
				ic("Not saved")
				
		ic(data)
		ic(root.saved_data)


class SaveAsButton(Button):
	def save_palette_as(self):
		root = self.parent.parent
		ids = root.ids
		root.filename = filedialog.asksaveasfilename(filetypes = [("Comma-separated Values", "*.csv")])

		ic()

		if root.filename:
			data = root.get_spinners_text()
			root.file_works.save_csv(root.filename, data)
			##root.saved = True
			root.saved_data = root.get_spinners_text()
		else:
			pass
		
		ic(root.saved_data)