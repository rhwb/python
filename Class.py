class ONS(object):

    def Message(self):
        print("Hello my friends!")

    def Add(self, a, b):
        c = int(a) + int(b)
        print("The result is {0}".format(c))




ref = ONS()
ref.Message()
ref.Add(1,2)




