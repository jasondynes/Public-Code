import colorgram

num_colour_extract = 300
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', num_colour_extract)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

# extracts colours from images using the colorgram package
rgb_list = []

for i in range(len(colors)):
    first_color = colors[i]
    rgb = first_color.rgb # e.g. (255, 151, 210)
    rgb_list.append((rgb.r, rgb.g, rgb.b))

print(colors)
print(rgb_list)
print(len(colors))




