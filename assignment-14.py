#program-1
x=[1,2,3,4,5]
a=[j**3 for j in x]
print(a)

#program-2
a=[i for i in range(2,30)  for j in range(2,i) if(i%j==0)  ]
b=[i for i in range(2,30) if(i not in a )]
print(b)

#program-3
'''
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.'''

#program-4
Celsius = [39.2 ,36.5, 37.3, 37.8]
fre=list(map(lambda a: 1.8*a+32,Celsius))
print(fre)

#program-5
lists=[1,2,3,4,5]
def squart(n):
    a=n*n
    return(a)
s=list(map(lambda n:squart(n),lists))
print(s)

#program-6
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
def prime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n
    
p=list(filter(lambda n: prime(n),lst))
print(p)

#program-7
lst=[1,2,3,4,5,5]
from  functools import *
m=reduce(lambda x,y:x*y,lst)
print(m)
    
    
