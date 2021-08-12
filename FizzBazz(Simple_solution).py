fizz = int(input('Enter first number'))
bazz = int(input('Enter second number'))
numbers = int(input())

for numbers in range (1,numbers+1):
    if (numbers %fizz==0) and (numbers %bazz==0):
        print ('FB', end=' ')
    elif (numbers %fizz==0):
        print ('F', end=' ')
    elif (numbers %bazz==0):
        print ('B', end=' ')
    else:
        print (numbers, end=' ')
