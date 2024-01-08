import re

print("Learning Regex Expression....")
print()
print()

# comments
print("")
print("")
print("")

print("^The.*Spain$ ==>> using ^ -> Start with, .* -> any character with 0 and more occurance, $ -> End with")
txt = "The rain in Spain"
x1 = re.search('^The.*Spain$', txt)
print(x1)
print()

print("he.*o ==>> using .* = any character with 0 and more oocurance")
txt2 = "hello hebbo hessssso hexxxxxxxxxxxxxxo"
x2 = re.findall("he.*o", txt2)
print(x2)
print()

print("he.{2}o ==>> using . = any character, {} -> exact number of occurance")
txt3 = "hello hebbo hessssso hexxxxxxxxxxxxxxo ninja ninja ninja"
x3 = re.findall("he.{2}o", txt3)
#x3 = re.findall("/ninja/gi", txt3)
print(x3)
print()

print("[abc123]000 ==>> using [] character set - each character either one of it must match. eg [123] -> 1 or 2 or 3")
print(re.findall("[abc123]000", "a000 1000"))
print()

print("[^abc123]000 ==>> using [^] character set - to exclude each character either one of it eg [^123] -> not 1 or not 2 or not 3")
print(re.findall("[^abc123]000", "a000 1000 z000"))
print()

# range character set
print("[a-zA-Z]inja ==>> usign the - as range")
print(re.findall("[a-zA-Z]inja", "ainja Binja dinja Minja"))
print("")

# range character set with exact size - eg. 10 digits only
print("[0-9]{10} ==>> usign the - as range and curly bracket to limit the number to 10 total numbers only")
print(re.findall("[0-9]{10}", "0123456789 101234567890 12345 1234567890"))
print("")

# range character set with exact size and limit range
# {,} can also use as {,5} = whatever but not more than 5 or {5,} = at least 5 characters but no limit on the max
print("[a-z]{3,5} ==>> only take words that has 3 to 5 characters are acceptable. eg: dog tame years")
print(re.findall("[a-z]{3,5}", "dog cat tame years to expected"))
print("")

print("Start and End characters using ^ and $. This can help to limit the total needed characters")
print(re.findall("^[a-zA-Z]{5}$", "tests"))
print("")

print("(cat|dog|mouse|mothing)? available ==>> using the () = limit the expression area and | for optional")
print(re.findall("(cat|dog|mouse|mothing)? available", "cat available, dog available, available"))
print("")

print("Username must be alphanumeric and contains 5-12 characters")
print(re.search("^\w{5,12}$", 'sharizan'))
print()

print("Email must be a valid address, eg: me@mydomain.com")
print(re.findall("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", "sharizan_81@yahoo.com"))
print()



