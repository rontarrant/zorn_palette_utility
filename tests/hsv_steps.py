def lerpcolourhsv(rgb1, rgb2, steps):
	#convert rgb to hsv
	r1, g1, b1 = rgb1
	r2, g2, b2 = rgb2
	rdelta, gdelta, bdelta = (r2-r1) / steps, (g2-g1) / steps, (b2-b1) / steps

	rgb_colour_list = []
	
	for step in range(steps):
		r1 += rdelta
		g1 += gdelta
		b1 += bdelta
		rgb_colour_list.append((r1, g1, b1))
		 
	return rgb_colour_list

##########
## tests #
##########

rgb_one = [255, 206, 25]
rgb_two = [35, 71, 149]

colour_list = lerpcolourhsv(rgb_one, rgb_two, 5)

for colour in colour_list:
	print(colour)
