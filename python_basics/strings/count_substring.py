def count_substrings(string, substring):
    substring_count = 0
    while string.find(substring) != -1:
        substring_count += 1
        start_index = string.find(substring)
        sub_len = len(substring)
        new_index = start_index + sub_len
        string = string[new_index:]
    return substring_count

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0