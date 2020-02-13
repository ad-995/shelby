#!/usr/bin/python3
import getpass, socket
from Crypto.PublicKey import RSA

class SSH_KEYS:
	def __init__(self,public,private):
		self.public = public
		self.private = private

def gen():
	username = getpass.getuser()
	hostname = socket.gethostname()

	key = RSA.generate(1024)

	pubkey = key.publickey()

	private_key = key.exportKey('PEM').decode('utf-8')

	public_key = pubkey.exportKey('OpenSSH').decode('utf-8')
	public_key = '%s %s@%s' % (public_key,username,hostname)

	keys = SSH_KEYS(public_key,private_key)
	return keys