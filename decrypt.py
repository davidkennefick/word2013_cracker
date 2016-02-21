#!/usr/bin/env python
import os
import re
import sys
import datetime
import subprocess
from subprocess import check_output
import hashlib
import getopt
import win32com.client as win32
from HashGen import HashGen #import the encryptor so we can use it here
from PasswordTrier import PasswordTrier #import the bruteforcer so we can use it here
'''
try:
    decrypt = sys.argv[1]
except:
    print "*** You need to supply a filename argument ***"
'''
def results(val1,val2):
    print "----------------------------------------------"
    if val1 == val2:
        print "Result : Both before and after hash values are the same "
    else:
        print "Result : Both before and after hash values are not the same "

#Function to kick it all off
def start():

    decrypt = "C:\Users\DavidK\Documents\College\Semester 2\Mobile Data Forensics\Labs\Lab3\decrypt\MDF-SF2.docx" #File the we want to crack
    wordlist = r"C:\Users\DavidK\Documents\College\Semester 2\Mobile Data Forensics\Labs\Lab3\decrypt\4to5_abcde012345.txt"
    print "Getting hash of " + decrypt
    originalHash = HashGen.sha1Encode(decrypt) #get the sha1 hash of the file
    print "The Sha1Encode value of the file is  : " ,originalHash

    print "Attempting to crack file " + decrypt
    print "##############################################################"
    print "Starting Brute force : ", datetime.datetime.now().time() #print current time
    result = PasswordTrier.crackFile(wordlist,decrypt) #get the pin

    print "Password is " ,result #print the password
    print "Finished Brute force : ", datetime.datetime.now().time() #print the current time
    print "##############################################################"
    print "Hashing file again"
    print "Getting hash of " + decrypt
    print "##############################################################"
    secondHashValue = HashGen.sha1Encode(decrypt) #get the sha1 hash of the file
    print "The Sha1Encode value of the file is  : " ,secondHashValue
    #print "Finished Hash : ", datetime.datetime.now().time()

    print "Generating results"
    results(originalHash,secondHashValue) #call conclusion function to compair the two hashes

start() #call the start function

'''
hash_raw = check_output(["python", "office2john.py", decrypt])
hash = hash_raw[0:-4]
cracker = "4321"'''
#cracker = check_output(["hashcat-cli64.exe", "-a", "0", "-m", "9600", "--username", hash])
#cudaHashcat64.exe -a 0 -m 9600 --username
'''
def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def crackfile(cracker,decrypt):
    word = win32.Dispatch("Word.Application")
    password_file = open(wordlist, 'r')
    passwords = password_file.readlines()
    password_file.close()
    passwords = [item.rstrip('\n') for item in passwords]
'''
