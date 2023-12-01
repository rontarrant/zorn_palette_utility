import csv
import os
import sys

## This puts us in the Python script"s directory instead of the Python
## executable directory or, when running from NotePad++, its
## program folder.
scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

## The file we write to is a concatenation of scriptdir, the file name
## and a directory delimiter in between...
## NOTE: Python won"t give permission to overwrite, so we have to find
## a way around it, perhaps with os.rename().
file_name = "zorn_colours.csv"
write_path = scriptdir + "/" + file_name

## The data we're going to write:
spinner_data = ["colour_01_spinner", "colour_02_spinner", "mix_01_spinner", "mix_02_spinner"]
colour_data = ["Ultramarine Blue", "Cadmium Yellow Medium", "Phthalo Green", "Ivory Black"]

## To avoid creating a blank line in the .csv file (Windows 10),
## specify the newline character as being blank. This overrides
## the Windows/DOS thing of using CR/LF where UNIX only uses LF.
## Here's how to define it:
##    newline = ""
with open(write_path, mode = "w", newline = "") as outfile:
	## I'm assuming this is a file handle complete with details for the write
	zorn_colour_handle = csv.writer(outfile, delimiter = ",", quotechar = "'", quoting = csv.QUOTE_MINIMAL)

	## Each of these lines writes a csv row to the file, first the headers, then the data.
	zorn_colour_handle.writerow(spinner_data)
	zorn_colour_handle.writerow(colour_data)

## This may not be necessary, but it's always a good idea.
outfile.close()
