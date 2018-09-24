n = int(input('How big is the square? '))
counter_1 = 0
counter_2 = 0
while counter_1 < n:
    counter_2 = 0
    while counter_2 < n:
        print("*", end="")
        counter_2+=1
    counter_1 +=1
    print() 

