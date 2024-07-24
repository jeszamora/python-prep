def yelling(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(yelling('my name jeff'))
print(yelling('please'))