#!/usr/bin/env python3

# Define the greetings method
def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

# Call the method with different test cases
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
