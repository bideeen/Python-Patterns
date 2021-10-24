# Inverted Pyramid
# number of rows
rows = 5
b = 0
# reverse the loops of the rows
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=' ')
    print('\r')