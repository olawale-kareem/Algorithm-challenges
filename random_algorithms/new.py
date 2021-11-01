# Task
# In this challenge you parse RGB colors represented by strings. The formats are primarily used in HTML and CSS. Your task is to implement a function which takes a color as a string and returns the parsed color as a map (see Examples).
# Input
# The input string color represents one of the following:

# 1. 6-digit hexadecimal
# "#RRGGBB" - Each pair of digits represents a value of the channel in hexadecimal: 00 to FF
# 2. 3-digit hexadecimal
# "#RGB" - Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.
# 3. Preset color name
# You have to use the predefined map PRESET_COLORS (Ruby, Python, JavaScript), presetColors (Haskell), or preset-colors (Clojure). The keys are the names of preset colors in lower-case and the values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

# Specification
# parse_html_color(color)
# Takes a String that represents a color and returns the parsed color as a map.

# Parameters
# color: String - A color represented by color name, 3-digit hexadecimal or 6-digit hexadecimal
# Return Value
# dict - A set of numerical RGB values
# Examples
# color	Return Value
# "#80FFA0"	{"r":128,"g":255,"b":160}
# "#3B7"	{"r":51,"g":187,"b":119}
# "LimeGreen"	{"r":50,"g":205,"b":50}


# print(hex(80))

# print(hex('limegreen'))

# print(hex(3))

# name = 'limegreen' 
# key = ''
# for i in name:
#     key += str(ord(i))
# print(hex(int(key)))



# print(hex(00),hex(11),hex(22))
# print(int('80FFA0', base=16))

#
# print(128/80)

# print(hex(32))




# def parse_html_color(color):
#   # seperate the hex code from ordinary numbers
#   if '#' not in color:
#       color_hex_code = PRESET_COLORS[color.lower()]
#       return color_hex_code
#   return color


