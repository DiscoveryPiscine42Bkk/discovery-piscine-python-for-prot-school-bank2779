while True:
    user_input = input("What you gotta say? : ")
    if user_input.strip().upper() == "STOP":
        print("I got that!")
        break
    print("I got that! Anything else?")