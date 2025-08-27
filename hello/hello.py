#fizz buzz

for i in range (31):
    if i%3 == 0  and i%5!= 0:
        print('Fizz')
    elif i%5 == 0 and i%3!= 0:
        print('Buzz')
    elif i%3 == 0 and i%5 == 0:
                print ('FizzBuzz')
    else:
        print(i)
        

#geometric sequence
x = 2

for g in range (10):
    print(x)
    x *= 2
    
#cubes

for t in range (5):
    print(t * t * t)
    
#fibonacci sequence
a = 0
b = 1

print(a + b)

for i in range (10):
    i = a+b
    print(i)
    a = b
    b = i


