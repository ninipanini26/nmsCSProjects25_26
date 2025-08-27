def isVampire(hour, awake):
    if ((6 > hour or 22 < hour) and awake == True):
        return True
    elif (6 < hour and 22 > hour and awake == False):
        return False
    else:
        return False

print(isVampire(20, True))
print(isVampire(15, False))

def testIsVampire(hour, awake, expected):
    result = isVampire(hour, awake)
    if (result == expected):
        print ("yayy!!!")
    else: 
        print ("Booo")


print(testIsVampire(5, True, True))
print(testIsVampire(3, False, False))
    