from os import path
import re

InputFile = input("Please enter the name of your file to be encrypted... \n")
Output = "Encrypted.txt"

if path.exists(InputFile) == False:
    print("The input file does not exist!")
    exit()
else:
    File = open(InputFile, "r")
    data = File.read()
    File.close()

OutFile = open(Output,"w")
for char in reversed(data):
    ascii_num = ord(char)
    ascii_num = ascii_num + 7
    OutFile.write(chr(ascii_num))
OutFile.close()





