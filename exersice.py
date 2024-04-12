# Arithmetic operators 
a = int(input("enter a number A: "))
b = int(input("enter the exponential of A: "))
p = a ** b
print(a,"to the power of", b, "is: ", p)
q = a / b
print(a, "divided by ",b, 'is: ', q)
y = a % b
print(a, 'modulus', b, 'is:', y)

# precedence of arithmetic operators
z = (a + b) -  5 * 2
print(z)
