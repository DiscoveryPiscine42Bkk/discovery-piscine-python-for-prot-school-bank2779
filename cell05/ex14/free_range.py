import sys

# Check if exactly two parameters are passed
if len(sys.argv) != 3:
    print("none")
else:
    # Convert the parameters to integers
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # Construct an array using the range function
    result = list(range(start, end + 1))
    
    # Display the array
    print(result)
