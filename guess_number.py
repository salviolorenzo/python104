import random
#secret_number = random.randint(1,10)
#guess_count = 5
#print("I am thinking of a number between 1 and 10. ")
#user_guess = int(input("What's the number? "))
#while guess_count >= 0:
#    while user_guess != secret_number:
#        user_guess = int(input("What's the number? "))
#        print('Nope, try again. ')
#        if user_guess > secret_number:
#            print('%d is too high.' %user_guess)
#        elif user_guess < secret_number:
#            print('%d is too low.' % user_guess)
#        print('You have %d guesses left.'%guess_count)
#        guess_count -=1   
#    print('You win!')

print('I am thinking of a number between 1 and 10.')
secret_number = random.randint(1, 10)
guesses = 5
user = int(input("What's the number? "))
if user != secret_number:
    while user != secret_number:
        print('Nope, try again.')
        if user > secret_number:
            print('%d is too high.'%user)
        elif user < secret_number:
            print('%d is too low.' %user)
        user = int(input("What's the number? "))
        guesses -=1
        print('You have %d guesses left.'%guesses)
        if guesses == 0:
            print('You lose.')
else:    
    print('You win!') 