## colour_calculations_fractional.py
## calculate and set all colour chips in the array.
from magic_palette_colorkit_fractional import ColourLookUp as clu

chip_set = None

class ColourCalculations():
	def blend_50_50(self, colour_01, colour_02):
		## break the colours out into RGBA values
		c1_r, c1_g, c1_b, al_1 = self.separate_rgba(colour_01)
		c2_r, c2_g, c2_b, al_2 = self.separate_rgba(colour_02)

		## mix components
		red = (c1_r + c2_r) / 2
		green = (c1_g + c2_g) / 2
		blue = (c1_b + c2_b) / 2
		alpha = (al_1 + al_2) / 2
		
		## return as a tuple
		return (red, green, blue, alpha)


	def blend_75_25(self, colour_01, colour_02):
		## break the colours out into RGBA values
		c1_r, c1_g, c1_b, al_1 = self.separate_rgba(colour_01)
		c2_r, c2_g, c2_b, al_2 = self.separate_rgba(colour_02)

		## mix components
		red = ((c1_r * 3) + c2_r) / 4
		green = ((c1_g * 3) + c2_g) / 4
		blue = ((c1_b * 3) + c2_b) / 4
		alpha = ((al_1 * 3) + al_2) / 4
		
		## return as a tuple
		return (red, green, blue, alpha)


	def separate_rgba(self, colour):
		## break the colours out into RGBA values
		red = colour[0]
		green = colour[1]
		blue = colour[2]
		alpha = colour[3]

		return red, green, blue, alpha


	def look_up_mix(self, chip_set, mix_colour_name):
		midpoint_colour = None
		
		for item in chip_set:
			if len(item) > 1:
				if item[2] == mix_colour_name:
					midpoint_colour = item[0]

		##ic(midpoint_colour)
		return midpoint_colour


	def set_spinner_defaults(self, ids, new = False):
		## Make sure both base colours and mix colours are set to a default
		## before proceeding.
		spin_01 = ids.colour_01_spinner.text
		spin_02 = ids.colour_02_spinner.text
		mix_01 = ids.mix_01_spinner.text
		mix_02 = ids.mix_02_spinner.text
		
		## If no colour is selected for a Spinner,
		## set it to the default (Titanium White)
		## so we don't get an ab-end.
		if spin_01 == "Colour 1" or new == True:
			ids.colour_01_spinner.text = "Titanium White"

		if spin_02 == "Colour 2" or new == True:
			ids.colour_02_spinner.text = "Titanium White"

		if mix_01 == "Tint 1" or new == True:
			ids.mix_01_spinner.text = "Titanium White"

		if mix_02 == "Tint 2" or new == True:
			ids.mix_02_spinner.text = "Titanium White"

	
	def set_colours(self, ids):
		self.set_spinner_defaults(ids)
		
		## The first six chips to be set are midpoint colours.
		##
		## A midpoint colour look-up is based on the contents of two spinners,
		## one of those at the top of the grid and the other on the left side.
		## This is the 'cheat' that allows us to (more or less) simulate a
		## subtractive colour space.
		##
		## Once these are set, all other chips are a mixture of colours
		## already set in the grid.
		##
		## This function could be shortened by building a list of working_chip_set's,
		## another list of mixing_colours to look up within each working_chip_set,
		## and a third list of chip numbers to be set as midpoint colours, thus
		## allowing them to be shoved off into another file and all this could
		## be done in a short loop.
		##
		## To deal with setting the chips after that in a second loop, another
		## set of lists would need to be built to hold:
		## mix_01 chip id's, and
		## mix_02 chip id's.
		## But this second loop could only set 11 of the remaining colour chips.
		## After that, yet another loop would have to deal with four-colour mixes.
		## But those aren't all 50/50 mixes. Some are 75/25 and that just 
		## complicates things.
		##
		## The only purpose it would serve to do all this is to cut the
		## set_colours() method down to size. It's my conviction that opening
		## such a can of worms wouldn't really make things better, just harder
		## for future readers to understand what's going on here.
		
		## chip_02 - midpoint colour look-up
		working_chip_set = clu[ids.colour_01_spinner.text]
		##ic(working_chip_set, ids.colour_02_spinner.text)
		midpoint_colour = self.look_up_mix(working_chip_set, ids.colour_02_spinner.text)
		ids.chip_02.dynamic_colour = midpoint_colour

		## chip_15 - midpoint colour look-up
		working_chip_set = clu[ids.mix_01_spinner.text]
		midpoint_colour = self.look_up_mix(working_chip_set, ids.mix_02_spinner.text)
		ids.chip_15.dynamic_colour = midpoint_colour

		## chip_31 - midpoint colour look-up
		working_chip_set = clu[ids.colour_02_spinner.text]
		midpoint_colour = self.look_up_mix(working_chip_set, ids.mix_02_spinner.text)
		ids.chip_31.dynamic_colour = midpoint_colour

		## chip_04 - midpoint colour look-up
		working_chip_set = clu[ids.colour_01_spinner.text]
		midpoint_colour = self.look_up_mix(working_chip_set, ids.mix_01_spinner.text)
		ids.chip_04.dynamic_colour = midpoint_colour
		
		## chip_27 - midpoint colour look-up
		working_chip_set = clu[ids.colour_01_spinner.text]
		midpoint_colour = self.look_up_mix(working_chip_set, ids.mix_02_spinner.text)
		ids.chip_27.dynamic_colour = midpoint_colour
		
		## chip_08 - midpoint colour look-up
		working_chip_set = clu[ids.mix_01_spinner.text]
		midpoint_colour = self.look_up_mix(working_chip_set, ids.colour_02_spinner.text)
		ids.chip_08.dynamic_colour = midpoint_colour

		## chip_20
		mix_01 = ids.chip_08.dynamic_colour
		mix_02 = ids.chip_31.dynamic_colour
		ids.chip_20.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_29
		mix_01 = ids.chip_27.dynamic_colour
		mix_02 = ids.chip_31.dynamic_colour
		ids.chip_29.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_01
		mix_01 = ids.colour_01.dynamic_colour
		mix_02 = ids.chip_02.dynamic_colour
		ids.chip_01.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_03
		mix_01 = ids.chip_01.dynamic_colour
		mix_02 = ids.colour_02.dynamic_colour
		ids.chip_03.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_14
		mix_01 = ids.chip_08.dynamic_colour
		mix_02 = ids.chip_20.dynamic_colour
		ids.chip_14.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_26
		mix_01 = ids.chip_20.dynamic_colour
		mix_02 = ids.chip_31.dynamic_colour
		ids.chip_26.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_30
		mix_01 = ids.chip_29.dynamic_colour
		mix_02 = ids.chip_31.dynamic_colour
		ids.chip_30.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_28
		mix_01 = ids.chip_27.dynamic_colour
		mix_02 = ids.chip_29.dynamic_colour
		ids.chip_28.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_21
		mix_01 = ids.chip_15.dynamic_colour
		mix_02 = ids.mix_02.dynamic_colour
		ids.chip_21.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_09
		mix_01 = ids.mix_01.dynamic_colour
		mix_02 = ids.chip_15.dynamic_colour
		ids.chip_09.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_06
		mix_01 = ids.chip_04.dynamic_colour
		mix_02 = ids.chip_08.dynamic_colour
		ids.chip_06.dynamic_colour = self.blend_50_50(mix_01, mix_02)

		## chip_16
		mix_01 = ids.chip_04.dynamic_colour
		mix_02 = ids.chip_27.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_15.dynamic_colour
		mix_05 = ids.chip_20.dynamic_colour
		mix_06 = self.blend_75_25(mix_04, mix_05)
		ids.chip_16.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_10
		mix_01 = ids.chip_04.dynamic_colour
		mix_02 = ids.chip_16.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_09.dynamic_colour
		mix_05 = ids.chip_14.dynamic_colour
		mix_06 = self.blend_75_25(mix_04, mix_05)
		ids.chip_10.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_22
		mix_01 = ids.chip_16.dynamic_colour
		mix_02 = ids.chip_27.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_21.dynamic_colour
		mix_05 = ids.chip_26.dynamic_colour
		mix_06 = self.blend_75_25(mix_04, mix_05)
		ids.chip_22.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_05
		mix_01 = ids.chip_04.dynamic_colour
		mix_02 = ids.chip_06.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_01.dynamic_colour
		mix_05 = ids.chip_28.dynamic_colour
		mix_06 = self.blend_75_25(mix_04, mix_05)
		ids.chip_05.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_07
		mix_01 = ids.chip_06.dynamic_colour
		mix_02 = ids.chip_08.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_03.dynamic_colour
		mix_05 = ids.chip_30.dynamic_colour
		mix_06 = self.blend_75_25(mix_04, mix_05)
		ids.chip_07.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_18
		mix_01 = ids.chip_16.dynamic_colour
		mix_02 = ids.chip_20.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_06.dynamic_colour
		mix_05 = ids.chip_29.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_18.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_17
		mix_01 = ids.chip_16.dynamic_colour
		mix_02 = ids.chip_18.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_05.dynamic_colour
		mix_05 = ids.chip_23.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_17.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_19
		mix_01 = ids.chip_18.dynamic_colour
		mix_02 = ids.chip_20.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_07.dynamic_colour
		mix_05 = ids.chip_30.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_19.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_24
		mix_01 = ids.chip_18.dynamic_colour
		mix_02 = ids.chip_29.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_22.dynamic_colour
		mix_05 = ids.chip_26.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_24.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_12
		mix_01 = ids.chip_06.dynamic_colour
		mix_02 = ids.chip_18.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_10.dynamic_colour
		mix_05 = ids.chip_14.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_12.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_11
		mix_01 = ids.chip_10.dynamic_colour
		mix_02 = ids.chip_12.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_05.dynamic_colour
		mix_05 = ids.chip_17.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_11.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_13
		mix_01 = ids.chip_12.dynamic_colour
		mix_02 = ids.chip_14.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_07.dynamic_colour
		mix_05 = ids.chip_19.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_13.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_23
		mix_01 = ids.chip_22.dynamic_colour
		mix_02 = ids.chip_24.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_17.dynamic_colour
		mix_05 = ids.chip_28.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_23.dynamic_colour = self.blend_50_50(mix_03, mix_06)

		## chip_25
		mix_01 = ids.chip_24.dynamic_colour
		mix_02 = ids.chip_26.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_19.dynamic_colour
		mix_05 = ids.chip_30.dynamic_colour
		mix_06 = self.blend_50_50(mix_04, mix_05)
		ids.chip_25.dynamic_colour = self.blend_50_50(mix_03, mix_06)

## In-file tests
## Run this file to see the test results.
if __name__ == "__main__":

	def to_ps(rgba):
		red = rgba[0]
		green = rgba[1]
		blue = rgba[2]
		
		red_str = str(round(red * 255))
		green_str = str(round(green * 255))
		blue_str = str(round(blue * 255))
		
		return (red_str, green_str, blue_str)
		
	
	## tests
	colcalc = ColourCalculations()
	
	## colours to work with...
	colour_01 = (0.996078431, 0.996078431, 0, 1)
	colour_02 = (0.141176471, 0.282352941, 0.588235294, 1)
	midpoint_colour = (0.168627451, 0.560784314, 0.411764706, 1)
	
	ic("For a visual check in Photoshop:")
	ic("colour_01: ", to_ps(colour_01))
	ic("colour_02: ", to_ps(colour_02))
	ic("midpoint: ", to_ps(midpoint_colour))

	## test 50/50
	colour_01_midpoint = colcalc.blend_50_50(colour_01, midpoint_colour)
	ic("50/50 colour_01 & midpoint: ", to_ps(colour_01_midpoint))
	
	midpoint_colour_02 = colcalc.blend_50_50(midpoint_colour, colour_02)
	ic("50/50 midpoint & colour_02: ", to_ps(midpoint_colour_02))
	
	## test 75/25
	midpoint_75_25_colour_01 = colcalc.blend_75_25(midpoint_colour, colour_01)
	ic("75/25 midpoint & colour_01: ", to_ps(midpoint_75_25_colour_01))

	## test 25/75
	colour_01_27_25_midpoint = colcalc.blend_75_25(colour_01, midpoint_colour)
	ic("75/25 colour_01 & midpoint: ", to_ps(colour_01_27_25_midpoint))

	ic("---------------------- testing complete------------------------")
	
	
