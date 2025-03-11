import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

num = 0

while num <= 10:
    output = f"Table de {num}:"
    i = 0
    
    while i <= 10:
        output += f" {num * i}"
        i += 1
    
    print(output)
    num += 1