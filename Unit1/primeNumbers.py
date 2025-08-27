def primeNumbers(n):
    for i in range (2, n-1):
        if (n%i ==0 and n!= i):
            return (i)
        else:
            return ("prime!")
        
print(primeNumbers(10))
print(primeNumbers(4))
print(primeNumbers(10))