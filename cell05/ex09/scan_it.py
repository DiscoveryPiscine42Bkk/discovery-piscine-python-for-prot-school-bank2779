#!/usr/bin/env python3
import sys

# Check if exactly two parameters are passed
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]

    # Count the number of times the keyword appears in the string
    count = string.count(keyword)

    # If the keyword appears at least once, print the count, otherwise print "none"
    if count > 0:
        print(count)
    else:
        print("none")
