def starts_with(s, p):
    return s.startswith(p)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True       