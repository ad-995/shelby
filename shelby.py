#!/usr/bin/python3
import os
from time import gmtime, strftime
from lib import logger, arguments, shells, cradles

def main():
	args = arguments.get_args() # get all the arguments
	absolute_path = os.path.dirname(os.path.realpath(__file__))
	absolute_path=str(absolute_path).replace('/lib','/')
	# generate_all_shells() runs through all the various shells that are in shelby and replaces the templates and writes them out to args.payload_directory; it returns a list of shell objects.
	all_shells = shells.generate_all_shells() # This purely configures the shells and writes them to ./web_delivery.

	# print some useful stuff
	print("The Web Delivery Server is at: %s:%s"  % (logger.red_fg(args.ip_address), logger.red_fg(args.web_delivery)))
	print("Shells receiving at: %s:%s"  % (logger.red_fg(args.ip_address), logger.red_fg(args.cradle_port)))
	print("Writing payloads to: %s" % logger.red_fg(args.payload_directory))
	print()

	# print out the available shells
	if all_shells != None:
		logger.heading('Shells')
		for shell in all_shells:
			logger.bullet('%s: %s' % (logger.yellow_fg(shell.name),shell.location))

	# same thing as generate_all_shells()
	all_cradles = cradles.generate_all_cradles(all_shells)

	with open('cradle_commands.txt','a') as f:
		time_of_run = strftime("%d/%m/%y, %H:%M:%S", gmtime())
		f.write('%s\n%s\n' % (time_of_run,'='*len(time_of_run)))
		logger.heading('Cradles')
		for counter,cradle in enumerate(all_cradles):
			print('%s %s' % (logger.yellow_fg('[-]'),cradle.name))
			logger.green.fg(cradle.execution)
			f.write('[%s] %s:\n%s\n\n' % (counter,cradle.name,cradle.execution))
			print()

	print('[%s]\tWritten by %s & %s (%s)'% (logger.yellow_fg('+'),logger.yellow_fg('@michaelranaldo'),logger.yellow_fg('@mez-0'),logger.yellow_fg('https://ad-995.group')))
if __name__ == "__main__": main()
