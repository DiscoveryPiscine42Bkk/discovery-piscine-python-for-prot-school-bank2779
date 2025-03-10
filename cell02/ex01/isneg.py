number = input("Enter a number: ")

try:
    num = int(number)
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
