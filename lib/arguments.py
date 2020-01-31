import argparse

def get_args():
	parser = argparse.ArgumentParser(description = "Giver of shells")
	parser.add_argument('-i', '--ip-address', metavar="",help="Attacker IP Address", required=True)
	parser.add_argument('-c', '--cradle-port', metavar="", help="Port for receiving shells")
	parser.add_argument('-w', '--web-delivery', metavar="", help="Port for serving shells")
	parser.add_argument('-d', '--payload-directory', default="./web_delivery/",metavar="", help="Directory for generated payloads")
	parser.add_argument('-D', '--resource-directory', default="./resources/",metavar="", help="Directory for shell resources")
	parser.add_argument('--randomize-names', action="store_true", help="Rename retrieved-shells to random string")
	args = parser.parse_args()
	if not any(vars(args).values()):
		parser.print_help()
		quit()
	else:
		return args