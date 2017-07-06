number = input("Enter your number: ")
num1 = int(number)

if num1 > 100:
    print("A")

    if num1 > 500:
        print("1")
    else:
        print("2")
else:
    print("B")

    if num1 < 50:
        print("4")
    else:
        print("3")

