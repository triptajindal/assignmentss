#make a list
l1=[]
n=int(input("no of inputs"))
for i in range (0,n):
    a=input()
    l1.append(a)
print(l1)

#add two list
l2=['google','apple','facebook','microsoft','tesla']
l3=[]
b=len(l2)
c=n+b;
for i in range(0,n):
    l3.append(l1[i])
for j in range(0,5):
    l3.append(l2[j])
print(l3)

#count no of times an object occur
l4=['1','2','1','2','3','1']
print(l4.count('1'))

#create list nd sort
l5=[]
n=int(input("no of inputs"))
for i in range (0,n):
    a=int(input())
    l5.append(a)
l5.sort()
print(l5)

#merge two array nd sort
a=[1,4,8]
b=[3,5]
c=a+b;
c.sort();
print(c);


#even odd no in a list
l6=[1,2,1,3,1,4,1]
c=0
count=0
for i in l6:
    if not i % 2:
        count=count+1
    else:
        c=c+1
print("even no.",count)
print("odd no.",c)

#reverse a tupple
a=(1,2,3)
b=a[::-1]
print(b)

#find min nd max of tupple
a=(1,2,3,4,5)
print(min(a))
print(max(a))

#string to be uppercase
s="hello"
print(s.upper())

#tell string to be numeric or not
s=input("enter string")
print(s.isdigit())


#replace world with name
s="hello world"
print(s.replace("world","tripta jindal"))
