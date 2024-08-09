my_list = [6, 3, 0, 11, 20, 4, 17]


index = 0

while index < len(my_list):
    digit = my_list[index]
    if digit % 2 == 0:
        print(digit)
    index += 1

print('\n')

for digit in my_list:
    if digit % 2 != 0:
        print(digit)