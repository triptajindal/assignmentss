## FILE HANDLING

# Question 1

f = open('abcd.txt','r')
l = f.readlines()
for i in l:
    print(i)
f.close()


# Question 2

from collections import Counter
with open('abcd.txt','r') as f:
    a = Counter(f.read().split())
    print(a)


# Question 3

with open('abcd.txt','r') as f:
    with open('new.txt','w') as g:
        for l in f:
            g.write(l)

# Question 4

with open('abcd.txt') as f:
    with open('new.txt') as g:
        for l1,l2 in zip(f,g):
            print(l1+l2)

# Question 5

num = ['4', '2', '10', '8','7','12','99','1','66','3']

with open('abc.txt', 'w') as filehandle:  
    for listitem in num:
        filehandle.write('%s\n' % listitem)

f=open("test.txt")
num=[]
for l in f:
    num.append(int(l))
num.sort()
f.close
with open('news.txt', 'w') as filehandle:  
    for listitem in num:
        filehandle.write('%s\n' % listitem)




