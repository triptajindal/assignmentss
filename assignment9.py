# program-1

# Here,in this program ZeroDivisionError error can occur nd it can be handle
a = 3
try:
    if a < 4:
        a = a / (a - 3)
        print(a)
except ZeroDivisionError:
    print("zero can't be divided")



# program-2

# here,in this IndexError will occur nd it can also be handle
try:
    l = [1, 2, 3]
    print(l[3])
except IndexError:
    print("index is out of range plz enter correct index")



# program-3
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise

#output--yes it throw an error as NameError is not used correctly here  hi there is not define
#and then raise do nothing


#program - 4

output - -
-5.0
a / b
result in 0




# program-5

# import error
try:
    import foo
except ImportError:
    foo = None  # now foo always exists

if foo:  # if the module is present
    foo.say_foo()
else:
    print("foo")  # IF NOT PRESENT

# value error
try:
    age = int(input("enter age of female "))
except ValueError:
    print("i donot understand character value")
else:
    print(age)

# index error
l = [1, 2, 3, 4, 5]
try:
    print(l[7])
except IndexError:
    print("index out of range")
