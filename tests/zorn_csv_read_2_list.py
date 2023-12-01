import csv
import os
import sys

## get the current directory of the script we're running
scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))
## the file we're going to open and...
file_name = 'zorn_colours2.csv'
## the full path to the file
full_path = scriptdir + '/' + file_name

print(full_path) ## proof that it's working so far

## prep to read the .csv contents into a form we can use
spinner_dictionary = {}
spinners = []
colours = []

## open the file
with open(os.path.join(full_path)) as csv_file:
	## read the contents into a list (in this case, a 2D list)
	csv_reader = list(csv.reader(csv_file, delimiter = ','))
	line_count = 0
	
	print("csv_reader: ", csv_reader) ## proof it's a 2D list
	
	for row in csv_reader:
		if line_count == 0:
			## the header row is the names of the Zorn App Spinners
			spinners = list(row)
			line_count += 1
		else:
			## the second row is the colours set in the Zorn App Spinners
			colours = list(row)

print("spinners: ", spinners)
print("colours: ", colours)

## convert into a 2D list where each spinner name is paired with its colour
both = list(zip(spinners, colours))

for item in both:
	print("spinner/colour pair: ", item)
