weather = 'snowy'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab you umbrella.')
    case _:
        print("Let's stay inside.")