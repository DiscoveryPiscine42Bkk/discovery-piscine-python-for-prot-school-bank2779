#!/usr/bin/env python3
import sys

# Define the method
def downcase_it(text):
    return text.lower()

# Check if any parameters are given
if len(sys.argv) < 2:
    print("none")
else:
    # Apply downcase_it to each parameter and print the result
    for arg in sys.argv[1:]:
        print(downcase_it(arg))
