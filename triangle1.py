num = int(input('Enter number of rows: '))
char = '*'
rows = 0
cols = 0
while rows < num:
    cols = 0
    while cols < num - rows - 1:
        print(end = ' ')
        cols+=1
    cols = 0
    while cols < rows + 1:
        print(char, end = ' ')
        cols+=1
    print() 
    rows+=1

#for i in range(0, num): #rows
#   for j in range(0, num - i - 1): #columns
#       print(end = ' ')
#   for j in range(0, i + 1):
#       print(emoji, end = ' ')
#   print()
