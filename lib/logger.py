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

class icons:
	def bullet():
		return u'\u2022'

def bullet(string):
	b = icons.bullet()
	print('\t%s\t%s' % (b,string))

def heading(msg):
	msg = '[+]     %s' % msg
	l = len(msg)
	print('%s\n\r%s' % (red_fg(msg),'='*l))