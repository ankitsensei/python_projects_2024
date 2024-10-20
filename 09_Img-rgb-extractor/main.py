import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.jpg', 6)

# Access the first color
first_color = colors[0]

# Get RGB, HSL, and proportion of the first color
rgb = first_color.rgb 
hsl = first_color.hsl  
proportion = first_color.proportion 

# Accessing Red component and Saturation with indexing
red = rgb[0]  
saturation = hsl[1] 