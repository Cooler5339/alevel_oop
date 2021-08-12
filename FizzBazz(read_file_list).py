
numbers = []

with open(r"/Users/vladymir/Documents/test/numb.rtf") as f:
    for numb in numbers:
        for num in range(1, numb[2]+1):
            if num % numb[0] == 0 and num % numb[1] == 0:
                print('FB', end=' ')
            elif num % numb[0] == 0:
                print('F', end=' ')
            elif num % numb[1] == 0:
                print('B', end=' ')
            else:
                print(num, end=' ')
