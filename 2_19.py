# Raad Barnett 1231583
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))

servings = int(input("How many servings does this make?\n\n"))
print("Lemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar\n".format(agave_nectar_cups))

servings_to_make = int(input("How many servings would you like to make?\n\n"))
ratio_servings = servings_to_make/servings

print("Lemonade ingredients - yields {:.2f} servings".format(servings_to_make))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups*ratio_servings))
print("{:.2f} cup(s) water".format(water_cups*ratio_servings))
print("{:.2f} cup(s) agave nectar\n".format(agave_nectar_cups*ratio_servings))


print("Lemonade ingredients - yields {:.2f} servings".format(servings_to_make))
print("{:.2f} gallon(s) lemon juice".format((lemon_juice_cups*ratio_servings)/16))
print("{:.2f} gallon(s) water".format((water_cups*ratio_servings)/16))
print("{:.2f} gallon(s) agave nectar".format((agave_nectar_cups*ratio_servings)/16))


# FIXME (1): Finish reading other items into variables, then output the three ingrdients
   
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons
   
