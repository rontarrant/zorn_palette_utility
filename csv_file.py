import csv
import os
import sys

class FileWorks():
	working_dir = None
	
	def __init__(self, **kwargs):
		## set to the Python script's working directory
		self.working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
		
	def load_csv(self, file_name):
		spinners = []
		colours = []
		ic(file_name)
		## open the file
		with open(file_name) as csv_file:
			csv_reader = list(csv.reader(csv_file, delimiter = ','))
			
		spinners = csv_reader[0]

		return spinners


	def save_csv(self, full_file_name, data):
		extension = ".csv"
		ic(full_file_name)
		if full_file_name[-4:] != extension:
			full_file_name = full_file_name + extension
			
		with open(full_file_name, mode = "w", newline = "") as outfile:
			zorn_file_handle = csv.writer(outfile, delimiter = ",", quotechar = "'", quoting = csv.QUOTE_MINIMAL)
			zorn_file_handle.writerow(data)

		outfile.close()

## ------------------------------ tests --------------------------------
if __name__ == "__main__":
	file_works = FileWorks()
	load_file_name = 'zorn_colours.csv'
	save_file_name = "zorn_colours.csv"

	## test file loading
	spinner_load = file_works.load_csv(load_file_name)
	
	for row in spinner_load:
		ic(row)
	## test file saving
	## The data we're going to write:
	spinner_data = ["colour_01_spinner", "colour_02_spinner", "mix_01_spinner", "mix_02_spinner"]
	colour_data = ["Ultramarine Blue", "Cadmium Yellow Medium", "Phthalo Green", "Ivory Black"]
	
	file_works.save_csv(save_file_name, [spinner_data, colour_data])


