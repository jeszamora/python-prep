def extract_language(language_code):
    split_code = language_code.split('_')
    return split_code[0]

def extract_region(lang_code):
    lang_rm = lang_code.split('_')[1]
    return lang_rm.split('.')[0]


def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    greeting = {
        'en': {'US': 'Hey!',
               'GB': 'Hello!',
               'AU': 'Howdy!',
        },
        'fr': 'Salut!',
        'pt': 'Ola!',
        'de': 'Hallo!',
        'sv': 'Hej!',
        'af': 'Haai!',
    }

    if language == 'en':
        return greeting[language][region]
    else:
        return greeting[language]
    

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
