input1 = input("Enter your Salary: ")
grade = input("Input your Grade:  ")
dept = input("Input your Department: ")

salary = int(input1)
lowtax = 10
special = "CTO"

if salary > 15000:
    if dept.lower() == "it":
        if grade == special:
            tax = 0;
            print("Your have been taxed %d" %tax)
        else:
            if int(grade) <= lowtax:
                tax = salary * 0.09
                print("Your have been taxed %d" %tax)
            elif int(grade) > lowtax:
                tax = salary * 0.15
                print("Your have been taxed %d" %tax)

        bonus = (salary - tax) * 0.05
        print("Your bonus is %d" % bonus)

        finalsal = salary - tax + bonus
        print("Your annual salary is %d" %finalsal)

    elif dept.lower() == "hr":
        if grade == special:
            tax = salary * 0.02
            print("Your have been taxed %d" %tax)
        else:
            if int(grade) <= lowtax:
                tax = salary * 0.09
                print("Your have been taxed %d" %tax)
            elif int(grade) > lowtax:
                tax = salary * 0.17
                print("Your have been taxed %d" %tax)

        finalsal = salary - tax
        print("Your annual salary is %d" % finalsal)
else:
    finalsal = salary
    print("Your annual salary is %d" %finalsal)








