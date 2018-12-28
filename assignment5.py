#verify a leap year
y=int(input("enter a year "))
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

#check whelther it is square or rect
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("Its a square")
else:
    print("Its a rectangle")

#input of 3 nd find oldest nd youngest
a=int(input("enter the age of first person"))
b=int(input("enter the age of second person"))
c=int(input("enter the age of third person"))
if(a>=b and a>=c):
    print(a,"is the oldest one")
elif (b >= a and b >= c):
    print(b, "is the oldest one")
else:
    print(c,"is the oldest one")

if (a <= b and a <= c):
    print(a, "is the youngest one")
elif (b <=a and b <=c):
    print(b, "is the youngest one")
else:
    print(c,"is the youngest one")


#enter age ,sex so tell there place of work
age=int(input("enter age"))
sex=input("tell whether the person is F or M")
if(sex=='F'):
    print("Work only in urban areas")
elif (sex=='M' and (age>20 and age<40)):
    print("Work anywhere")
elif (sex=='M' and (age>40 and age<60)):
    print("Work in urban areas")
else:
    print("ERROR")


#tell the cost nd give discount
q=int(input("Tell the quantity"))
c=q*100
if(c>1000):
    ans=(c*10)/100
    c=c-ans
    print("Total Cost is ",c)
else:
    print("Total Cost is ",c)


#take 10 integers nd print them on screen
for i in range(0,10):
    a=int(input())
    print(a)

#infinte loop
num=True
while(num==True):
    print("a")


#new list store the square of old one
n = int(input("no of element to be list"))
l = []
l2 = []
for i in range(0, n):
    a = int(input())
    l.append(a)
for j in l:
    l2.append(j * j)
print(l2)


#divide in,string,float
lists=[1,2,'h',1.2,'e']
l1=[]
l2=[]
l3=[]
for i in lists:
    print(i)
    if type(i)==int:
        l1.append(i)
    elif type(i)== str:
        l2.append(i)
    else:
        l3.append(i)
print("interer list",l1)
print("string list",l2)
print("floats list",l3)


#prime question
for num in range(1,101):
  if num>1:
    isDivisible=False
    for index in range(2,num):
        if num %index==0:
            isDivisible=True
    if not isDivisible:
        print(num)


#pattern question
for i in range(1, 5):
    k = 0
    for j in range(1, 5):
        if (i == j):
            while (k != j):
                print("*", end=' ')
                k = k + 1
    print()


#make list find an element and delete it
n = int(input("no of element to be list"))
l = []
for i in range(0, n):
    a = int(input())
    l.append(a)
no = int(input())
for i in l:
    if (no == i):
        l.remove(i)
print(l)
