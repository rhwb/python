InputFile = input("Please enter the name of your file... \n")
Extension = ".txt"
check = input("What character do you want to search for? \n")
replace = input("What do you want to this character with? \n")
Output = input("What is the name of the file to be created? \n")
Length = len(check)



File = open(InputFile + Extension, "r")
data = File.read()
File.close()

OutFile = open(Output + Extension,"w")
for char in data:
    if data.find(check):
        OutFile.write(replace)
    else:
      OutFile.write(char)
OutFile.close()

