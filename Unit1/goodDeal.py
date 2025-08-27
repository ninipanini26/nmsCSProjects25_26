def goodDeal(originalPrice, salePrice):
    if(salePrice < originalPrice * 0.75):
        return True
    else:
        return False

def isGoodDeal(originalPrice, salePrice, expected):
    result = goodDeal(originalPrice, salePrice)
    if(result == expected):
        print ("yayy!!!")
    else:
        print ("false")

print(isGoodDeal(100, 74, True))
print(isGoodDeal(100, 75, False))