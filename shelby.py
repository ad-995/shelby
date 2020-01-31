#!python3
from lib import logger, arguments, shells, cradles

def main():
	args = arguments.get_args() # get all the arguments

	# if no callback port is set, default it to 4444.
	if args.cradle_port != None:
		cradle_port = args.cradle_port
	else:
		cradle_port = "4444"

	# same as above, if no web delivery port is set; default to 80
	if args.web_delivery != None:
		web_delivery = args.web_delivery
	else:
		web_delivery = "80"

	# generate_all_shells() runs through all the various shells that are in shelby and replaces the templates and writes them out to args.payload_directory; it returns a list of shell objects.
	all_shells = shells.generate_all_shells() # This purely configures the shells and writes them to ./web_delivery.

	# print some useful stuff
	print("The Web Delivery Server is at: %s:%s"  % (logger.red_fg(args.ip_address), logger.red_fg(web_delivery)))
	print("Shells receiving at: %s:%s"  % (logger.red_fg(args.ip_address), logger.red_fg(cradle_port)))
	print("Writing payloads to: %s" % logger.red_fg(args.payload_directory))
	print()

	# print out the available shells
	logger.heading('Shells')
	for shell in all_shells:
		logger.bullet('%s: %s' % (logger.yellow_fg(shell.name),shell.location))

	# same thing as generate_all_shells()
	all_cradles = cradles.generate_all_cradles(all_shells)

	logger.heading('Cradles')
	for cradle in all_cradles:
		print('%s %s' % (logger.yellow_fg('[-]'),cradle.name))
		logger.green.fg(cradle.execution)
		print()

	print('[%s]\tWritten by %s & %s (%s)'% (logger.yellow_fg('+'),logger.yellow_fg('@michaelranaldo'),logger.yellow_fg('@mez-0'),logger.yellow_fg('https://ad-995.group')))
if __name__ == "__main__": main()
