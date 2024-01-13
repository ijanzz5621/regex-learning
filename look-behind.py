import re

print()
print("LOOK BEHIND: ?<=")
print("================")
print("find the next text that start with name: by using look behind")

regex = r"(?<=name: )[a-zA-Z]+"
text = "This is a sample text to test. name: Sharizan Redzuan. "

print(f"Sample text: {text}")
print(f"Regex: {regex}")

# find the next text that start with name: by using look behind
result = re.findall(regex, text)

# result = Sharizan
print("Result:")
print(result)

print()
print("INVERTED LOOK BEHIND: ?<!")
print("=========================")
print("find the next text that not start with name: by using inverted look behind")

regex = r"(?<!name: )[a-zA-Z]+"
text = "This is a sample text to test. name: Sharizan Redzuan. "

print(f"Sample text: {text}")
print(f"Regex: {regex}")

# find the next text that start with name: by using look behind
result = re.findall(regex, text)

# result = Sharizan
print("Result:")
print(result)