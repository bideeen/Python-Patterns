# Pyramid Pattern Number

# number of rows
rows = 5
# Ask for input from the user
# rows = int(input('Enter the number of rows: '))

# Outer loop(Rows)
for i in range(1, rows+1):
    # Nested loops(Columns)
    for j in range(1, i+1):
        # display the number
        print(j, end=' ')
    # a new line after each row
    print('')


