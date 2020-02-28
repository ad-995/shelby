#!/usr/bin/python3
import re,os,mimetypes,random,string,shutil,errno
from lib import logger,arguments

cpp_function_regex = re.compile(r'^(\w+)\s(\w+)\((.*)\)')
regex_global_namespace_usage = re.compile(r'(^\w+)(\:\:)(\w+)(.*)')

used_random_names = []

class CPP:
	def __init__(self,full,type,name,args,newname):
		self.full = full
		self.type = type
		self.name = name
		self.args = args
		self.newname = newname

class GNS:
	def __init__(self,full,namespace,seperator,function,args,newname):
		self.full = full
		self.namespace = namespace
		self.seperator = seperator
		self.function = function
		self.args = args
		self.newname = newname

def copy(src, dest):
	try:
		print('Copied %s to %s' % (logger.green_fg(src),logger.green_fg(dest)))
		shutil.copytree(src, dest)
		return True
	except OSError as e:
		if e.errno == errno.ENOTDIR:
			print('Copied %s to %s' % (logger.green_fg(src),logger.green_fg(dest)))
			shutil.copy(src, dest)
			return True
		else:
			print('%s already exists' % logger.red_fg(dest))
			return False

def random_string():
	letters = string.ascii_lowercase+string.ascii_uppercase
	r = ''.join(random.choice(letters) for i in range(16))
	if r not in used_random_names:
		return r
	else:
		r = random_string()

def empty_cpp_files(root):
	all_files = get_all_files(root)
	cpp_files = get_cpp_files(all_files)
	for cpp_file in cpp_files:
		open(cpp_file, 'w').close()


def get_all_files(root):
	files_sorted = []
	for path, subdirs, files in os.walk(root):
	    for name in files:
	    	p = os.path.join(path, name)
	    	if p not in files_sorted:
	    		files_sorted.append(p)
	if len(files) == 0:
		return None
	else:
		return files_sorted

def get_cpp_files(files):
	cpp_files = []
	for f in files:
		mime = mimetypes.guess_type(f)
		if mime[0] != None:
			if 'text/x-c++src' in mime[0]:
				if f not in cpp_files:
					cpp_files.append(f)
	if len(cpp_files) == 0:
		return None
	else:
		return cpp_files

def create_cpp_objs(cpp_files):
	cpp_objs = []
	for cpp in cpp_files:
		with open(cpp,'r') as f:
			for line in f:
				match = cpp_function_regex.search(line)
				if match != None:
					full = match.group(0)
					type = match.group(1)
					name = match.group(2)
					args = match.group(3)
					newname = random_string()
					cpp_obj = CPP(full,type,name,args,newname)
					if cpp_obj not in cpp_objs:
						cpp_objs.append((cpp_obj))
	if len(cpp_objs) == 0:
		return None
	else:
		return cpp_objs

def create_globalnamespace(cpp_files):
	gns_objs = []
	for cpp in cpp_files:
		with open(cpp,'r') as f:
			for line in f:
				match = regex_global_namespace_usage.search(line)
				if match != None:
					full = match.group(0)
					namespace = match.group(1)
					seperator = match.group(2)
					function = match.group(3)
					args = match.group(4)
					newname = random_string()
					args = match.group(3)
					if namespace.startswith('I'):
						continue
					gns_obj = GNS(full,namespace,seperator,function,args,newname)
					if gns_obj not in gns_objs:
						gns_objs.append(gns_obj)
	if len(gns_objs) == 0:
		return False
	else:
		return gns_objs

def do_change(cpp_objs,line):
	for cpp_obj in cpp_objs:
		regex_function_usage = re.compile(r'[\s\,\.\(](%s)[\.\(]' % cpp_obj.name)

		function_match = re.search(regex_function_usage,line)
		namespace_match = re.search(regex_global_namespace_usage,line)

		if function_match != None:
			if ' wmain(' not in line:
				line = re.sub(function_match.group(1),cpp_obj.newname,line)
				return line
	return line

	# for gns_obj in gns_objs:
	# 	if gns_obj.namespace in line and gns_obj.function in line:
	# 		return line.replace(gns_obj.namespace,gns_obj.newname).replace(gns_obj.function,gns_obj.newname)

	# 	elif gns_obj.namespace in line and gns_obj.function not in line:
	# 		return line.replace(gns_obj.namespace,newname)

	# 	elif gns_obj.function in line and gns_obj.namespace not in line:
	# 		return line.replace(gns_obj.function,newname)
	# 	else:
	# 		return line

def do_name_change(cpp_files,cpp_objs,gns_objs,new_directory,original_root_dir):
	empty_cpp_files(new_directory)
	for cpp_file_path in cpp_files:
		with open(cpp_file_path,'r') as f:
			for line in f:
				line = line.strip('\n')
				if len(line) != 0:
					line = do_change(cpp_objs,line)
					write(line,cpp_file_path,new_directory,original_root_dir)

def write(line,current_cpp_file_path,new_directory,original_root_dir):
	current_directory = current_cpp_file_path.rsplit('/',1)[0]
	current_file = current_cpp_file_path.split('/')[-1]
	new_path = current_directory.replace(original_root_dir,new_directory)+'/'+current_file
	with open(new_path,'a') as f:
		f.write(line+'\n')

def obfuscate():
	args = arguments.get_args()
	logger.heading('C++ Obfuscation')
	print('%s: This is an experimental function and it only works on C++ projects.' % logger.yellow_fg('WARNING'))

	working_directory = args.experimental_args

	if working_directory == None:
		logger.red.fg('Please specify a a directory containing a cpp project!')
		quit()

	new_directory = './experimental_obfuscation/'
	print('Writing to: %s' % logger.red_fg(new_directory))

	original_root_dir = working_directory[:working_directory.rindex('/')]+'/'

	copy(working_directory,new_directory)

	all_files = get_all_files(working_directory)
	if all_files == None:
		print('No files found in %s!' % logger.red_fg(working_directory))
		return False

	cpp_files = get_cpp_files(all_files)
	if cpp_files == None:
		print('No cpp files found in %s!' % logger.red_fg(working_directory))
		return False

	cpp_objs = create_cpp_objs(cpp_files)
	if cpp_objs == None:
		logger.red.fg('Could not extract cpp functions from cpp files!')
		return False

	gns_objs = create_globalnamespace(cpp_files)
	if gns_objs == None:
		logger.red.fg('Could not extract global namespaces from cpp files!')
		return False
		
	do_name_change(cpp_files,cpp_objs,gns_objs,new_directory,original_root_dir)