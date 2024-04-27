class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfun(self):
        print("My name is :" + self.name)
        print("I am " + self.age)
p1 = Person("Lalit", "22")
p1.myfun()    