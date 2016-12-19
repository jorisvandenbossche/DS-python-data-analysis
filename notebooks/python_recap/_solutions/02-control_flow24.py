sentence = "hello world! 123"
d = {"DIGITS": 0, "LETTERS": 0}
for char in sentence:
    if char.isdigit():
        d["DIGITS"] += 1
    elif char.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])