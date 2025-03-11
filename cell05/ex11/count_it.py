#!/usr/bin/env python3
import sys

# Check if no parameters are passed
if len(sys.argv) == 1:
    print("none")
else:
    # Display the number of parameters
    print(f"parameters: {len(sys.argv) - 1}")
    
    # Iterate through the parameters and display each with its length
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
