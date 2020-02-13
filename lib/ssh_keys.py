#!/usr/bin/python3
import getpass, socket, os
from Crypto.PublicKey import RSA
from lib import arguments

args = arguments.get_args()
absolute_path = os.path.dirname(os.path.realpath(__file__))
absolute_path=str(absolute_path).replace('/lib','/')

class SSH_KEYS:
	def __init__(self,public,private):
		self.public = public
		self.private = private

def gen():
	username = getpass.getuser()
	hostname = socket.gethostname()

	key = RSA.generate(4096)

	pubkey = key.publickey()

	private_key = key.exportKey('PEM').decode('utf-8')

	public_key = pubkey.exportKey('OpenSSH').decode('utf-8')
	public_key = '%s %s@%s' % (public_key,username,hostname)

	keys = SSH_KEYS(public_key,private_key)
	if not os.path.exists(args.ssh_directory):
		os.makedirs(args.ssh_directory)

	with open(args.ssh_directory+'id_rsa.pub','w') as f:
		f.write(public_key)
	with open(args.ssh_directory+'id_rsa','w') as f:
		f.write(private_key)
	return keys