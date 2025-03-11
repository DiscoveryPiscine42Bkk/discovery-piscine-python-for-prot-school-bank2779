originalarray = [2, 8, 9, 48, 8, 22, -12, 2]
newarray = {x + 2 for x in originalarray if x > 5}
print(originalarray)
print(newarray)