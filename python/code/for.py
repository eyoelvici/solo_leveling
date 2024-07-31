for y in range(11):
    for x in range(11):
        if y%5==0:
            print('+' if x % 5 == 0 else '-', end='')
        else:
            print('+' if x % 5 == 0 else ' ', end='')

    print()

for y in range(11):  # Outer loop for 11 rows (y values from 0 to 10)
    for x in range(11):  # Inner loop for 11 elements in each row (x values from 0 to 10)
        if y % 5 == 0:  # Check if 'y' is a multiple of 5
            if x % 5 == 0:  # Check if 'x' is also a multiple of 5
                print('+', end='')  # Print '+' for a multiple of 5
            else:
                print('-', end='')  # Print '-' for non-multiples of 5
        else:  # If 'y' is not a multiple of 5
            if x % 5 == 0:  # Check if 'x' is a multiple of 5
                print('+', end='')  # Print '+' for a multiple of 5
            else:
                print(' ', end='')  # Print a space for non-multiples of 5
    print()  # Print a newline to start a new row
