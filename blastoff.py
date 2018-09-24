from time import sleep

count = int(input('Number to start countdown: '))
if count <= 20 and count > 0:
    message = input("What is your blastoff message? ")
    while count >= 0:
        print(count)
        sleep(1)
        count -=1
    print(message)
else: print('Enter a number 0-20.')