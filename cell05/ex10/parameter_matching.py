#!/usr/bin/env python3

import sys

# Check if exactly one parameter is passed
if len(sys.argv) != 2:
    print("none")
else:
    # The first parameter is stored in sys.argv[1]
    parameter = sys.argv[1]
    
    # Prompt the user to enter a word
    user_input = input("What was the parameter? ")
    
    # Compare the user's input with the passed parameter
    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
