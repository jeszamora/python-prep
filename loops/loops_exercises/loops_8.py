my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { string: len(string)
            for string in my_set
            if len(string) % 2 != 0 }

print(my_dict)