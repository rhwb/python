x = {74:'London',82:'New York',99:'Manchester'}

for a in x:
    print("{0}".format(x[a]))

print(x.get(74))

a = input("Enter the first number...")
b = input("Enter the seconf number")

try:
    c = a + b
    print(c/0)
except:
    print("Something went wrong!")

