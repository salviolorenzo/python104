width = int(input("Width? "))
height = int(input("Height? "))
counter_row = 0
counter_col = 0
while counter_row < height:
    counter_col = 0
    if counter_row == 0 or counter_row == (height-1):
        while counter_col < width:
            print('*', end='')
            counter_col+=1
    elif counter_row > 0 and counter_row < (height-1):
        while counter_col < width:
            if counter_col == 0 or counter_col == (width-1):
                print('*',end='')
            else:
                print(' ' , end='')
            counter_col+=1
    counter_row+=1
    print()