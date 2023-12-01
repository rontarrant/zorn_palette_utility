import csv
import os
import sys

working_dir = os.path.abspath(os.path.dirname(sys.argv[0])) ## current directory
load_file_name = 'zorn_colours.csv'


def load_csv(working_dir, file_name):
	spinner_dictionary = {}
	spinners = []
	colours = []
	load_path = working_dir + "/" + file_name

	## open the file
	with open(load_path) as csv_file:
		csv_reader = list(csv.reader(csv_file, delimiter = ','))
		line_count = 0
		
		for row in csv_reader:
			if line_count == 0:
				spinners = list(row)
				line_count += 1
			else:
				colours = list(row)

	both = list(zip(spinners, colours))
	return both


## tests
if __name__ == "__main__":
	spinner_load = load_csv(working_dir, load_file_name)
	for row in spinner_load:
		print(row)
