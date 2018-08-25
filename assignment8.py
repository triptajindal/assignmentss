#area and circumference of circle
class circle:
    def __init__(self,r):
        self.r=r
    def getArea(self):
        print("area of circe",3.14*self.r*self.r)
    def getCircumference(self):
        print("circumference of circe",2*3.14*self.r)
        
r=int(input())
c=circle(r)
c.getArea()
c.getCircumference()


#create student class nd some method
class student:
    def __init__(self):
        self.name=input()
        self.rollno=int(input())
    def setAge(self):
        self.age=int(input())
    def setMarks(self):
        self.marks=int(input())
    def display(self):
        print("name =",self.name," rollno =",self.rollno," age =",self.age," marks =",self.marks)

s=student()
s.setAge()
s.setMarks()
s.display()



#create temperature class
class temperature:
    def __init__(self,c,f):
        self.c=c
        self.f=f
    def convertFarenheit(self,c):
        print("farenheit = ",c*1.8+32)
    def convertCelsius(self,f):
        print("celsius = ",(f-32)/1.8)

c=int(input("enter celcius value"))
f=int(input("enter farenheit value"))
t=temperature(c,f)
t.convertFarenheit(c)
t.convertCelsius(f)


#movie detail and add one value
class movieDetails:
    def __init__(self,name,y,r):
        self.artistName = name
        self.year = y
        self.ratings = r
    def Add(self):
        self.movieName = input("Enter movie name: ")
    def Display(self):
        print("Movie Name:",self.movieName,"  Artist Name:",self.artistName,"  Year:",self.year,"  Ratings:",self.ratings)
name=input("enter name")
year=int(input("enter year"))
rating=input("enter rating")
obj = movieDetails(name,year,rating)
obj.Add()
obj.Display()




#create animal base class of tiger class
class Animal:
    def animal_attribute(self):
        print("animal")
class Tiger(Animal):
    def tiger(self):
        print("tiger")
a=Animal()
t=Tiger()
t.animal_attribute()


#what will be the output

OUTPUT==
1)'A','B'
2)'A','B'




#class shape rectangle nd square

class shape:
    def values(self):
        self.length=int(input("enter length"))
        self.breadth=int(input("enter breadth"))
    def area(self):
        area=self.length*self.breadth
        if self.length==self.breadth:
            print("square area = ",area)
        else:
            print("rectangle area = ",area)
class square(shape):
    def __init__(self):
        self.values()
        self.area()
class rectangle(shape):
    def __init__(self):
        self.values()
        self.area()
s=shape()
sq=square()
re=rectangle()

'''
        
