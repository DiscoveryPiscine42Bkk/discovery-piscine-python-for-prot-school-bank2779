#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) != 2:
    print("none")
else:
    # Get the string passed as a parameter
    string = sys.argv[1]
    
    # Find all occurrences of the character 'z' in the string
    z_count = string.count('z')
    
    # If there are any 'z' characters, print them; otherwise, print "none"
    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")
