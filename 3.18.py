import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}


# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input("Enter wall width (feet):\n"))
print('Wall area: {0} square feet'.format(wall_height*wall_width))
paint_needed = (wall_height*wall_width)/350
print("Paint needed: {:.2f} gallons".format(paint_needed))
cans_needed = round(paint_needed)
print("Cans needed: {0} can(s)\n".format(cans_needed))


color_paint = input("Choose a color to paint the wall:\n")
price_color = int(paint_colors[color_paint])
print("Cost of purchasing {0} paint: ${1}".format(color_paint,price_color*cans_needed))

   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
