def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(rows)