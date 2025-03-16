# Source folder: Class & Objects in Python

# assignment_1.py
# Define a python class Person with instance object variables name and age. Set instance object variables in the __init__() method. Also define the show() method to display the name and age of a person.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}")


person1 = Person("Sohan Sahoo", 69)
person1.show()


# assignment_2.py
# Define a class Circle with an instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setradius(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        return area

    def getCircumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference


circle1 = Circle(5)
print("Radius:", circle1.getradius())
print("Area:", circle1.getArea())
print("Circumference:", circle1.getCircumference())


# assignment_3.py
# Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions(), and getArea() methods.


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def showDimensions(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)

    def getArea(self):
        area = self.length * self.breadth
        return area


r1 = Rectangle(10, 5)
r1.showDimensions()
area = r1.getArea()
print("Area:", area)


# assignment_4.py
# Define a class Book with instance object variables bookid, title, and price. Initialize them via the __init__() method. Also define a method to show book variables.


class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def show(self):
        print("Book ID:", self.bookid)
        print("Title:", self.title)
        print("Price:", self.price)


book1 = Book(1, "Almanack of Naval Ravikant", 0.00)
book1.show()


# assignment_5.py
# Define a class Team with an instance object variable as a list of team member names. Provide methods to input member names and display member names.


class Team:
    def __init__(self):
        self.members = []

    def input_member(self, name):
        self.members.append(name)

    def display_members(self):
        print("Team members:", self.members)


t = Team()
t.input_member("Sohan")
t.input_member("Jane")
t.display_members()


