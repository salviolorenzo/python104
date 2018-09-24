#Algorithm Friyay
#Print numbers 1-100
#For every multiple of 3, print Fizz
#For every multiple of 5, print Buzz
#For every multiple of 3 and 5, print FizzBuzz

num = 1
while num < 100:
    if num%15 == 0:
        print('FizzBuzz')
    elif num %3 == 0:
        print ('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)
    num+=1