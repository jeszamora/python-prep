my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

list_index = 0
digit_index = 0

while list_index < len(my_list):
    while digit_index < len(my_list[list_index]):
        number = my_list[list_index][digit_index]
        if number % 2 == 0:
            print(number)
        digit_index += 1
    list_index += 1
    digit_index = 0

