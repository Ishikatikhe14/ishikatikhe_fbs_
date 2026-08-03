n = 5  # Number of rows

for i in range(1, n + 1):
    # Print leading spaces for alignment
    print(" " * (n - i), end="")
    
    if i == 1:
        # First row contains only '1'
        print("1")
    elif i == n:
        # Last row contains all numbers from 1 to n separated by a space
        print(" ".join(str(x) for x in range(1, n + 1)))
    else:
        # Intermediate rows start with '1' and end with the row number
        inner_spaces = " " * (2 * i - 3)
        print(f"1{inner_spaces}{i}")