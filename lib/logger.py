import os, math
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

# Switches
colour_status = True

def green_fg(string):
	string=str(string)
	if colour_status:
		return (colour_green_fg + string + colour_remove)
	else:
		return string

def green_bold(string):
	string=str(string)
	if colour_status:
		return (colour_green_bold + string + colour_remove)
	else:
		return string

def green_bg(string):
	string=str(string)
	if colour_status:
		return (colour_green_bg + string + colour_remove)
	else:
		return string

def red_fg(string):
	string=str(string)
	if colour_status:
		return (colour_red_fg + string + colour_remove)
	else:
		return string

def red_bold(string):
	string=str(string)
	if colour_status:
		return (colour_red_bold + string + colour_remove)
	else:
		return string

def red_bg(string):
	string=str(string)
	if colour_status:
		return (colour_red_bg + string + colour_remove)
	else:
		return string

def yellow_fg(string):
	string=str(string)
	if colour_status:
		return (colour_yellow_fg + string + colour_remove)
	else:
		return string

def yellow_bold(string):
	string=str(string)
	if colour_status:
		return (colour_yellow_bold + string + colour_remove)
	else:
		return string

def yellow_bg(string):
	string=str(string)
	if colour_status:
		return (colour_yellow_bg + string + colour_remove)
	else:
		return string

class green:
	def __init__(self,string):
		self.string = string

	def fg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(green_fg(string))

	def bg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(green_bg(string))

	def bold(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(green_bold(string))

	def heading(string):
		print(green_bold(string))

	def bullet(string):
		b = ' -'
		print('%s\t%s' % (green_fg(b),string))

class red:
	def __init__(self,string):
		self.string = string

	def fg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(red_fg(string))

	def bg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(red_bg(string))

	def bold(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(red_bold(string))

	def heading(string):
		print(red_bold(string))

	def bullet(string):
		b = ' -'
		print('%s\t%s' % (red_fg(b),string))

class yellow:
	def __init__(self,string):
		self.string = string

	def fg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(yellow_fg(string))

	def bg(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(yellow_bg(string))

	def bold(string):
		log_time=strftime("%d/%m/%y, %H:%M:%S", gmtime())
		print(yellow_bold(string))

	def heading(string):
		print(yellow_bold(string))

	def bullet(string):
		b = ' -'
		print('%s\t%s' % (yellow_fg(b),string))

def banner(msg):
	columns = os.get_terminal_size().columns # the length of the terminal
	msg = 'Todo List' # the main banner string
	title = (' ' * ((columns - len(msg))//2) + msg) # remove the length of the string from the available columns, then half it to get the middle
	border_length = (' ' * ((columns - len(msg))) + msg) # do the same, just dont diivide it. this gives the entire length of the terminal
	corner = '+'
	dividers = '-' * (columns - len(corner)*2)
	border = '%s%s%s' % (yellow_fg(corner),red_fg(dividers),yellow_fg(corner))
	print(border)
	print(yellow_fg(title))
	print(border)

class icons:
	def check():
		return u'\u2713'
	def cross():
		return u'\u2717'
