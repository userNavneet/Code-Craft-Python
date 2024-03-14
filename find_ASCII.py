# Program to find the ASCII value of the given character
usrInput = ''
while True:
    usrInput = input("Enter a single character as input: ")
    if len(usrInput) == 1:
        print("The ASCII value of '" + usrInput + "' is", ord(usrInput))
        break
    print("Please enter a single character to continue\n")
