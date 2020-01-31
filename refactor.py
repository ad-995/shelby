#!python3
from lib import logger, arguments, shells, cradles

def main():
	args = arguments.get_args()

	ipaddr = args.ip_address

	if args.cradle_port != None:
		cradle_port = args.cradle_port
	else:
		cradle_port = "4444"

	if args.web_delivery != None:
		web_delivery = args.web_delivery
	else:
		web_delivery = "80"

	all_shells = shells.generate_all_shells() # This purely configures the shells and writes them to ./web_delivery.

	# for shell in all_shells:
	# 	name = shell.name
	# 	type = shell.type
	# 	location = shell.location
	# 	content = shell.content
	# 	print(name,type,location)

	all_cradles = cradles.generate_all_cradles(all_shells)

if __name__ == "__main__": main()
