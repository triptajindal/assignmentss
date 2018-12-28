#reverse using list method
list=[1,2,3,4]
list.reverse()
print(list)

#print uppercase letter of a string
string="Hello WorlD"
for i in string:
    if(i.isupper()):
         print(i)

#split on user input from comma and made a list of it
a=input("enter a string")  #eg--1,2,33,566
l=[]
l1=[]
for i in a:
    l=a.split(",")
for i in l:
    l1.append(int(i))
print(l1)


#pallindrome or not

s1=input("enter string")
if(s1==''.join(reversed(s1))):
    print("pallindrome")
else:
    print("not pallindrome")

#shallow copy nd deep copy

#deep copy example
import copy
l1=[1,[3,7],[4,5],8]
l2=copy.deepcopy(l1)
l1[2][1]=99
print(l1)
print(l2)

#if b is a DEEP COPY of a,then b=[a copy];
#b nd a point to different location;

#shallow copy example
import copy
l1=[1,[3,7],[4,5],8]
l2=copy.copy(l1)
l1[2][1]=99
l1[0]=88
print(l1)
print(l2)

# if b is a SHALLOW COPY of a,for premitive data b=[a assign];and for objects b=[A retain];
#b nd a both point to same memory location


