def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)
