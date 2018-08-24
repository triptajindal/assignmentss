#user input dictionary through for loop-
d1={}
n=int(input())
for i in range(0,n):
    d1[i]=input()
print(d1)
ele=input()
flag= 0
for key in d1.keys():
    if d1[key]==ele:
        print(key)
        flag =1
        break
if flag==0:
    print("Key not found")


#nexted dictionary nd display particular students marks
d1={}
for i in range(1,3):
    d2={}
    n=input("enter name")
    for j in range(0,2):
        sub=input("enter sub")
        marks=int(input("enter marks"))
        d2[sub]=marks
    d1[n]=d2
print(d1)
stu=input()
print(d1[stu])

