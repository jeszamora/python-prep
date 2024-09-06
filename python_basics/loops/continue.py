# We have a list of strings and none values assigned to the variable 
# cities. We want to iterate over the list and print the length of 
# each string.
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        # We use the continue statement to skip forward to the 
        # next iteration of the nearest loop without executing the 
        # code in our for loop
        continue
    print(len(city))