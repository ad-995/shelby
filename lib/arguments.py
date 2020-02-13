import argparse
from lib import logger

def get_args():
	parser = argparse.ArgumentParser(description = "Giver of shells")
	parser.add_argument('-i', '--ip-address', metavar="127.0.0.1",help="Attacker IP Address")
	parser.add_argument('-p', '--shell-port', metavar="4444", default=str(4444),help="Port for receiving shells")
	parser.add_argument('-s', '--server-port', metavar="80", default=str(80),help="Port for serving shells")
	parser.add_argument('-C', '--cradle-directory', default="cradles/", metavar="cradles", help="Directory for generated payloads")
	parser.add_argument('-D', '--resource-directory', default="resources/",metavar="resources", help="Directory for shell resources")
	parser.add_argument('-S', '--ssh-directory', default="keys/",metavar="keys", help="Directory for SSH Keys")
	parser.add_argument('--linux', action="store_true", help="Only Linux shells")
	parser.add_argument('--windows',action="store_true", help="Only Windows shells")
	parser.add_argument('--randomize-names', action="store_true", help="Rename retrieved-shells to random string")
	parser.add_argument('--version', action="store_true", help="Print current version")
	args = parser.parse_args()

	if args.ip_address == None:
		logger.red.fg('Please specify an ip address!')
		quit()

	if args.version:
		version()
		quit()

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