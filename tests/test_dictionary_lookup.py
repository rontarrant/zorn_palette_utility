from magic_palette_fractional import ColourLookUp as clu


def look_up_base(base_colour_name):
	chip_set = clu[base_colour_name]
	print(chip_set, "\n")
	
	return chip_set

def look_up_mix(chip_set, mix_colour_name):
	for item in chip_set:
		if len(item) > 1:
			if item[2] == mix_colour_name:
				print("mix colour: ", item[1])
				print("midpoint colour: ", item[0])

	
## get a chip set to work with
colour_name = "Ultramarine Blue"
chip_set = clu[colour_name]

print("Chip set:")
print(chip_set)
look_up_mix(chip_set, "Ivory Black")
