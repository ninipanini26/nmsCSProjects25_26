def Attention(n):
    if(n[0:8] == "Hey You!"): 
        return True
    else:
        return False

def AttentionTest(n, expected):
    correct = Attention(n)
    if (correct == expected):
        print("yayyy!!!!")
    else:
        print("Boooo")

print(AttentionTest("Hey You! You suck <3", True))