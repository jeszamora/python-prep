def intervals(integer):
    if 0 <= integer <= 50:
        print(f'{integer} is between 0 and 50')
    elif 51 <= integer <= 100:
        print(f'{integer} is between 51 and 100')
    elif integer > 100:
        print(f'{integer} is greater than 100')
    elif integer < 0:
        print(f'{integer} is less than 0')


intervals(10)
intervals(-10)
intervals(100) 
intervals(1000)