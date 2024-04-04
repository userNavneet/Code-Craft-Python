# Creation of strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("String 1:", string1)
print("String 2:", string2)

# Concatenation of strings
concatenated_string = string1 + " " + string2 if 'string1' in locals() and 'string2' in locals() else "Not enough strings to concatenate."

print("Concatenated string:", concatenated_string)

# Deletion of strings
del_string = input("Enter the string you want to delete (1 or 2): ")
if del_string == '1':
    del string1
    print("String 1 deleted.")
elif del_string == '2':
    del string2
    print("String 2 deleted.")
else:
    print("Invalid choice. No string deleted.")