number = 4936

one_place = number % 10

number //= 10

ten_place = number % 10

number //= 10

hundred_place = number % 10

number //= 10

thousand_place = number % 10

result = {
    'one_place': one_place,
    'ten_place': ten_place,
    'hundred_place': hundred_place,
    'thousand_place': thousand_place,
}

print(result)