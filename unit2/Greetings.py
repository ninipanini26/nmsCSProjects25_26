def Greetings(name):
    return("Hello," + name + ",how are you?")

def isGreetings(given, expected):
    result = Greetings(given)
    if(result == expected):
        print ("yayy!!!")
    else:
        print ("false")
print(isGreetings("ramya", "Hello," + "ramya" + ",how are you?"))

