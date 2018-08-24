# area and circumference of circle
class circle:
    r = int(input())

    def getArea(self):
        print("area of circe", 3.14 * self.r * self.r)

    def getCircumference(self):
        print("circumference of circe", 2 * 3.14 * self.r)


c = circle()
c.getArea()
c.getCircumference()


# create student class nd some method
class student:
    def __init__(self):
        self.name = input()
        self.rollno = int(input())

    def setAge(self):
        self.age = int(input())

    def setMarks(self):
        self.marks = int(input())

    def display(self):
        print("name =", self.name, " rollno =", self.rollno, " age =", self.age, " marks =", self.marks)


s = student()
s.setAge()
s.setMarks()
s.display()


# create temperature class
class temperature:
    def convertFarenheit(self, c):
        print("farenheit = ", c * 1.8 + 32)

    def convertCelsius(self, f):
        print("celsius = ", (f - 32) / 1.8)


c = int(input("enter celcius value"))
t = temperature()
t.convertFarenheit(c)
f = int(input("enter farenheit value"))
t.convertCelsius(f)


#  not attemped question 4



# create animal base class of tiger class
class Animal:
    def animal_attribute(self):
        print("animal")
class Tiger(Animal):
    def tiger(self):
        print("tiger")

a = Animal()
t = Tiger()
t.animal_attribute()



# what will be the output
OUTPUT ==
1) 'A', 'A'
2) 'A', 'B'




# class shape rectangle nd square
class shape:
    length = int(input())
    breadth = int(input())

    def area(self):
        area = self.length * self.breadth
        print(area)


class square(shape):
    def areas(self):
        print("square area= ")


class rectangle(shape):
    def areas(self):
        print("rectangle area= ")


s = shape()
sq = square()
re = rectangle()
sq.area()
re.area()
