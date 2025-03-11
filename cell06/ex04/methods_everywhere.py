import sys

# Method to shrink a string to the first 8 characters
def shrink(text):
    print(text[:8])

# Method to enlarge a string to 8 characters by appending 'Z'
def enlarge(text):
    print(text.ljust(8, 'Z'))

# Main logic to handle command-line arguments
if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)  # If exactly 8 characters, print as is
