user_choice = input("Please enter one of the following options: \n" "1 - Addition \n""2 - Subtraction \n"
"3 - Division \n""4 - Multiplication \n""5 - Timestable \n""6 - Quit \n")
menu_choice = int(user_choice)
def first_num():
    num1 = input("Please enter the first number: ")
    return num1
def second_num():
    num2 = input("Please enter the second number: ")
    return num2
def add(num1, num2):
    answer = num1 + num2
    return answer
def subtraction(num1, num2):
    answer = num1 - num2
    return answer
def division(num1, num2):
    answer = num1 / num2
    return answer
def multiplication(num1, num2):
    answer = num1 * num2
    return answer
def timestable(num1, num2):
    while num1 <= num2:
        for x in range(1, 11):
            answer = x * num1
            print("{0} * {1} = {2}".format(num1, x, answer))
        add1 = add1 + 1
def quit():
    ans = input("Do you want to repeat this process? Y/N \n")
    if ans.lower() == "n":
        exit()
    else:
        user_choice = input("Select a new menu option... ")
        menu_choice = int(user_choice)
while menu_choice <= 6:
    if menu_choice != 6:
        num1 = int(first_num())
        num2 = int(second_num())
        if menu_choice == 1:
            print(add(num1, num2))
            quit()
        elif menu_choice == 2:
            print(subtraction(num1, num2))
            quit()
        elif menu_choice == 3:
            print(division(num1, num2))
            quit()
        elif menu_choice == 4:
            print(multiplication(num1, num2))
            quit()
        elif menu_choice == 5:
            timestable(num1, num2)
            quit()
    else:
        quit = input("Are you sure you want to quit? Y/N")
        if quit.lower() == 'y':
            exit
        else:
            user_choice = input("Select a new menu option... ")
            menu_choice = int(user_choice)






