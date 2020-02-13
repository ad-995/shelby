import argparse

def get_args():
	parser = argparse.ArgumentParser(description = "Giver of shells")
	parser.add_argument('-i', '--ip-address', metavar="",help="Attacker IP Address", required=True)
	parser.add_argument('-p', '--shell-port', metavar="", default=str(4444),help="Port for receiving shells")
	parser.add_argument('-s', '--server-port', metavar="", default=str(80),help="Port for serving shells")
	parser.add_argument('-C', '--cradle-directory', default="cradles/",metavar="", help="Directory for generated payloads")
	parser.add_argument('-D', '--resource-directory', default="resources/",metavar="", help="Directory for shell resources")
	parser.add_argument('-S', '--ssh-directory', default="keys/",metavar="", help="Directory for SSH Keys")
	# parser.add_argument('-o', '--operating-system', default=None,metavar="", help="Generate specific OS Cradles")
	parser.add_argument('--linux', action="store_true", help="Only Linux shells")
	parser.add_argument('--windows',action="store_true", help="Only Windows shells")
	parser.add_argument('--randomize-names', action="store_true", help="Rename retrieved-shells to random string")
	args = parser.parse_args()

	if not args.cradle_directory.endswith('/'):
		args.cradle_directory = args.cradle_directory+'/'

	if not args.resource_directory.endswith('/'):
		args.resource_directory = args.resource_directory+'/'

	if not args.ssh_directory.endswith('/'):
		args.resource_directory = args.resource_directory+'/'

	if not any(vars(args).values()):
		parser.print_help()
		quit()
	else:
		return args