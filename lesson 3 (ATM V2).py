money = int(input('Withdrawal amount:'))
banknotes = [50,100,200,500,1000]
for i in banknotes:
    if money >= 0:
        change = money // i
        money -= change * i
        if change != 0:
         print ('Get your money!:'+str(change)+'*'+str(i)+'$')
else:
    print ('GoodBye! See later!')