import re

print()
print("LOOK AHEAD: ?=")
print("================")
print("find the next text that followed by Redzuan using look ahead")

regex = r"\b[a-zA-Z]+\b(?=\sRedzuan)"
text = "This is a sample text to test. name: Sharizan Redzuan. "

print(f"Sample text: {text}")
print(f"Regex: {regex}")

# find the next text that start with name: by using look behind
result = re.findall(regex, text)

# result = Sharizan
print("Result:")
print(result)

print()
print("INVERTED LOOK AHEAD: ?!")
print("================")
print("find the next text that not followed by Redzuan using inverted look ahead")

regex = r"\b[a-zA-Z]+\b(?!\sRedzuan)"
text = "This is a sample text to test. name: Sharizan Redzuan. "

print(f"Sample text: {text}")
print(f"Regex: {regex}")

# find the next text that start with name: by using look behind
result = re.findall(regex, text)

# result = Sharizan
print("Result:")
print(result)