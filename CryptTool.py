import base64
import os
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken


class CryptTool:
	def __init__(self):
		pass

	def get_hash(self,pwd):
		salt = "??TamaoWakayu987432@9450524879!!".encode()
		kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())
		hashed_str = base64.urlsafe_b64encode(kdf.derive(pwd.encode()))
		return hashed_str.decode()


if __name__ == '__main__':
	s = Cipher().get_hash("Xoromate324@")
	print(s.decode())