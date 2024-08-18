def greet(language):
    greeting = {
        'en': 'Hi!',
        'fr': 'Salut!',
        'pt': 'Ola!',
        'de': 'Hallo!',
        'sv': 'Hej!',
        'af': 'Haai!',
    }
    return greeting[language]

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!