from time import gmtime, strftime

# Colours
colour_green_fg = "\033[0;32m"
colour_green_bg = "\033[1;42m"
colour_green_bold = "\033[1;32m"

colour_red_fg = "\033[0;31m"
colour_red_bg = "\033[1;41m"
colour_red_bold = "\033[1;31m"

colour_yellow_fg = "\033[0;33m"
colour_yellow_bg = "\033[1;43m"
colour_yellow_bold = "\033[1;33m"

colour_remove= "\033[0m"

def green_fg(string):
	string=str(string)
	print(colour_green_fg + string + colour_remove)

def green_bold(string):
	string=str(string)
	print(colour_green_bold + string + colour_remove)

def green_bg(string):
	string=str(string)
	print(colour_green_bg + string + colour_remove)

def red_fg(string):
	string=str(string)
	print(colour_red_fg + ">> " + string + colour_remove)

def red_bold(string):
	string=str(string)
	print(colour_red_bold + string + colour_remove)

def red_bg(string):
	string=str(string)
	print(colour_red_bg + string + colour_remove)

def yellow_fg(string):
	string=str(string)
	print(colour_yellow_fg + string + colour_remove)

def yellow_bold(string):
	string=str(string)
	print(colour_yellow_bold + string + colour_remove)

def yellow_bg(string):
	string=str(string)
	print(colour_yellow_bg + string + colour_remove)
