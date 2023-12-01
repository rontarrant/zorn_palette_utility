## Colour Calculations

class ColourCalculations():
	def blend_50_50(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		alpha = 1 ## assume full strength
		
		## mix components
		red = round((c1_r + c2_r) / 2, 3)
		green = round((c1_g + c2_g) / 2, 3)
		blue = round((c1_b + c2_b) / 2, 3)
		alpha = round((c1_a + c2_a) / 2, 3)
		return (red, green, blue, alpha)


	def blend_33_66(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		
		## mix
		red = round((c1_r * .34) + (c2_r * .67), 3)
		green = round((c1_g * .34) + (c2_g * .67), 3)
		blue = round((c1_b * .34) + (c2_b * .67), 3)
		## alpha = (c1_a * .34) + (c2_a * .67)
		alpha = round(1.0, 3)
		
		return (red, green, blue, alpha)
		
	
	def blend_66_33(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		
		## mix
		red = round((c1_r * .67) + (c2_r * .34), 3)
		green = round((c1_g * .67) + (c2_g * .34), 3)
		blue = round((c1_b * .67) + (c2_b * .34), 3)
		alpha = round((c1_a * .67) + (c2_a * .34), 3)
		
		return (red, green, blue, alpha)
		
	
	def colour_blend(self, colour_01, colour_02):
		## break the colours out into RGB values
		c1_r, c1_g, c1_b, c1_a = self.separate_rgb(colour_01)
		c2_r, c2_g, c2_b, c2_a = self.separate_rgb(colour_02)
		
		alpha = 1 - (1 - c1_a) * (1 - c2_a)
		red = c1_r * c1_a / alpha + c2_r * c2_a * (1 - c1_a) / alpha
		green = c1_g * c1_a / alpha + c2_g * c2_a * (1 - c1_a) / alpha
		blue = c1_b * c1_a / alpha + c2_b * c2_a * (1 - c1_a) / alpha
		
		return (red, green, blue, alpha)


	def separate_rgb(self, colour):
		## break the colours out into RGB values
		red = colour[0]
		green = colour[1]
		blue = colour[2]
		alpha = colour[3]
		
		return red, green, blue, alpha


	def list_paint_chips(self, ids):
		for id in ids:
			print(id)

	
	def set_colours(self, ids):
		## mix and set chip_01
		mix_01 = ids.colour_01.dynamic_colour
		mix_02 = ids.colour_02.dynamic_colour
		ids.chip_01.dynamic_colour = self.blend_50_50(mix_01, mix_02)
		print("Chip 01: ", ids.chip_01.dynamic_colour)

		## mix and set chip_02
		mix_01 = ids.tint_01.dynamic_colour
		mix_02 = ids.tint_02.dynamic_colour
		ids.chip_02.dynamic_colour = self.blend_66_33(mix_01, mix_02)
		print("Chip 02: ", ids.chip_02.dynamic_colour)

		## mix and set chip_03
		mix_01 = ids.tint_01.dynamic_colour
		mix_02 = ids.tint_02.dynamic_colour
		ids.chip_03.dynamic_colour = self.blend_33_66(mix_01, mix_02)
		print("Chip 03: ", ids.chip_03.dynamic_colour)

		## mix and set chip_04
		mix_01 = ids.tint_01.dynamic_colour
		mix_02 = ids.colour_01.dynamic_colour
		ids.chip_04.dynamic_colour = self.blend_50_50(mix_01, mix_02)
		print("Chip 04: ", ids.chip_04.dynamic_colour)
		
		## mix and set chip_05
		mix_01 = ids.tint_02.dynamic_colour
		print("mix_01: ", ids.tint_02.dynamic_colour)
		mix_02 = ids.colour_02.dynamic_colour
		print("mix_02: ", ids.colour_02.dynamic_colour)
		ids.chip_05.dynamic_colour = self.blend_50_50(mix_01, mix_02)
		print("Chip 05: ", ids.chip_05.dynamic_colour)
		
		## mix and set chip_06
		mix_01 = ids.tint_02.dynamic_colour
		mix_02 = ids.chip_05.dynamic_colour
		mix_03 = self.blend_66_33(mix_01, mix_02)
		mix_04 = ids.colour_01.dynamic_colour
		ids.chip_06.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 06: ", ids.chip_06.dynamic_colour)

		## mix and set chip_07
		mix_01 = ids.chip_06.dynamic_colour
		mix_02 = ids.chip_05.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.chip_01.dynamic_colour
		ids.chip_07.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 07: ", ids.chip_07.dynamic_colour)

		## mix and set chip_08
		mix_01 = ids.tint_01.dynamic_colour
		mix_02 = ids.colour_02.dynamic_colour
		ids.chip_08.dynamic_colour = self.blend_50_50(mix_01, mix_02)
		print("Chip 08: ", ids.chip_08.dynamic_colour)

		## mix and set chip_09
		mix_01 = ids.colour_02.dynamic_colour
		mix_02 = ids.chip_05.dynamic_colour
		mix_03 = self.blend_66_33(mix_01, mix_02)
		mix_04 = ids.chip_02.dynamic_colour
		ids.chip_09.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 09: ", ids.chip_09.dynamic_colour)

		## mix and set chip_10
		mix_01 = ids.colour_02.dynamic_colour
		mix_02 = ids.chip_05.dynamic_colour
		mix_03 = self.blend_33_66(mix_01, mix_02)
		mix_04 = ids.chip_03.dynamic_colour
		ids.chip_10.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 10: ", ids.chip_10.dynamic_colour)

		## mix and set chip_11
		mix_01 = ids.chip_01.dynamic_colour
		mix_02 = ids.chip_07.dynamic_colour
		mix_03 = self.blend_50_50(mix_01, mix_02)
		mix_04 = ids.tint_01.dynamic_colour
		ids.chip_11.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 11: ", ids.chip_11.dynamic_colour)

		## mix and set chip_12
		mix_01 = ids.colour_01.dynamic_colour
		mix_02 = ids.chip_06.dynamic_colour
		mix_03 = self.blend_33_66(mix_01, mix_02)
		mix_04 = ids.chip_03.dynamic_colour
		ids.chip_12.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 12: ", ids.chip_12.dynamic_colour)

		## mix and set chip_13
		mix_01 = ids.colour_01.dynamic_colour
		mix_02 = ids.chip_07.dynamic_colour
		mix_03 = self.blend_33_66(mix_01, mix_02)
		mix_04 = ids.chip_03.dynamic_colour
		ids.chip_13.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 13: ", ids.chip_13.dynamic_colour)

		## mix and set chip_14
		mix_01 = ids.colour_01.dynamic_colour
		mix_02 = ids.chip_06.dynamic_colour
		mix_03 = self.blend_66_33(mix_01, mix_02)
		mix_04 = ids.chip_02.dynamic_colour
		ids.chip_14.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 14: ", ids.chip_14.dynamic_colour)

		## mix and set chip_15
		mix_01 = ids.chip_01.dynamic_colour
		mix_02 = ids.chip_07.dynamic_colour
		mix_03 = self.blend_66_33(mix_01, mix_02)
		mix_04 = ids.chip_02.dynamic_colour
		ids.chip_15.dynamic_colour = self.blend_50_50(mix_03, mix_04)
		print("Chip 15: ", ids.chip_15.dynamic_colour)
		
		print("")
	
if __name__ == "__main__":
	## tests
	colour_01 = (0.329, 0.016, 0.035, 1)
	colour_02 = (0.216, .012, 0.035, 1)

	## test 50/50
	colcalc = ColourCalculations()
	result = colcalc.blend_50_50(colour_01, colour_02)
	print("50/50: ", result)

	## test 33/66
	result = colcalc.blend_33_66(colour_01, colour_02)
	print("33/66: ", result)

	result = colcalc.blend_50_50(colour_01, colour_02)
	print("colour blend: ", result)
