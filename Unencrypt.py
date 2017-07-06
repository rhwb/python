from os import path

InputFile = "Encrypted.txt"
Output = "Un-encrypted.txt"

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
    ascii_num = ascii_num - 7
    OutFile.write(chr(ascii_num))
OutFile.close()