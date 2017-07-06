from_num = input("Times table from: ")
to_num = input("Times table to: ")
num1 = int(from_num)
num2 = int(to_num)

if num1 > num2:
    while num1 >= num2:
        for x in range(1,11):
            answer = x * num1
            print("{0} * {1} = {2}".format(num1, x, answer))
        num1 = num1 - 1
else:
    while num1 <= num2:
        for x in range(1,11):
            answer = x * num1
            print("{0} * {1} = {2}".format(num1, x, answer))
        num1 = num1 + 1




