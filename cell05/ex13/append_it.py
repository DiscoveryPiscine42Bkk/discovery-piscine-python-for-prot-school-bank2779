import sys

# Check if no parameters are passed
if len(sys.argv) == 1:
    print("none")
else:
    # Iterate through the parameters (starting from index 1 to skip the script name)
    for param in sys.argv[1:]:
        # Only process parameters that do not already end with "ism"
        if not param.endswith("ism"):
            print(f"{param}ism")
