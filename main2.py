import re

test_string = '123abc456789abc123ABC!@#$%_-aaabbbccc'

pattern = re.compile(r"abc") # r for raw

matches = pattern.finditer(test_string)

#matches = re.finditer(r"abc", test_string)

for match in matches:
    print(match)
    
# match() example - only match from the beginning

matches4 = pattern.match(test_string)

print(matches4)

# findall() example

matches2 = pattern.findall(test_string)

print(matches2)

# search() example

matches3 = pattern.search(test_string)

print(matches3)

# split()


# sub()
    



