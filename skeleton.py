class Shell:
	def __init__(self,name,type,location,content):
		self.name = name
		self.type = type
		self.location = location
		self.content = content

class Cradle:
	def __init__(self,name,execution,payload):
		self.name = name
		self.execution = execution
		self.payload = payload

cradles = []
shells = []

def nishang_reverse_tcp():
	name = 'Nishang Reverse TCP'
	type = 'Reverse TCP'
	location = './dir/file.ps1'
	content = open(location).read()
	shell = Shell(name,type,location,content)
	shells.append(shell)

def regsvr32():
	for payload in shells:
		cradle_name = 'regsvr32: %s' % payload.name
		payload = 'file/base64'
		execution = 'regsvr32.exe %s' % payload
		cradle = Cradle(cradle_name,execution,payload)
		cradles.append(cradle)

for cradle in cradles:
	print(vars(cradle))

for shells in shells:
	print(vars(shell))