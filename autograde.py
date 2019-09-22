#!/usr/bin/env python
import os
import subprocess

subprocess.call("rm -f ./a.out", shell=True)

retcode = subprocess.call("./test.sh", shell=True)

print ("Score: " + str(retcode) + " out of 2 correct.")
#print("*************Original submission*************")
#with open('add.go','r') as fs:
    #print(fs.read())
