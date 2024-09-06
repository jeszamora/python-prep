# Python uses zero based indexing
lst = [1, 3, 7, 15]
index = 0

# We create a while loop that iterates until the expression evaluates False
while index < len(lst):
    # We reference the list and use square brackets to index into it
    print(lst[index])
    # We increment our index
    index += 1