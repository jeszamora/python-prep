age = input('How old are you? ')

time = [10, 20, 30 , 40]

print(f'You are {age} years old.')

for years in time:
    print(f'In {years} years, you will be {int(age) + years} years old.')