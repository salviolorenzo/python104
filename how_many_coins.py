coin = 0
print('You have %d coins.' % coin)
question = input('Do you want another? ').lower()
#print(tally)
while question == 'yes':
    coin = coin + 1
    print('You have %d coins.' % coin)
    question = input('Do you want another? ').lower()
print('bye')



