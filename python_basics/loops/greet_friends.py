# We have a list of strings referenced by the variable friends
friends = ['Sarah', 'John', 'Hannah', 'Dave']

# We set up our for loop 
for friend in friends:
    # We call the print function and pass an f string as an argument. 
    # The f string allows us to interpolate various variables 
    # or expressions from our code
    print(f'Hello, {friend}!')