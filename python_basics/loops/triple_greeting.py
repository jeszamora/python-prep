greeting = 'Aloha!'

# We will create a loop to print out the value referenced be greeting 3 times


for _ in range(3):
    print(greeting)


# We initialize a counter variable.
greeting_count = 0

# We create a while loop that will iterate until the expression 
# greeting_count < 3 evaluates to false. 
while greeting_count < 3:
    # We invocate the print function passing the greeting variable 
    # as the argument
    print(greeting)
    # We increment our count
    greeting_count += 1