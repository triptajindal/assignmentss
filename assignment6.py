#print area of sphere
def area(r):
    area = 4 * (3.14) * r * r
    return (area)

r = int(input())
print(area(r))

#finf perfect no within range
def perfect(a, b):
    for j in range(a, b):
        sum = 0
        for i in range(1, j):
            if (j % i == 0):
                sum = sum + i
        if (sum == j):
            print(j, end=' ')

perfect(1, 1000)


#print multiplication table
def multiply(n):
    for i in range(1, 11):
        print(n, "*", i, "=", (n * i))

n = int(input())
multiply(n)


#power with recursion
def power(a, b):
    if b == 1:
        return a
    else:
        return a * power(a, b - 1)

a = int(input())
b = int(input())
print(power(a, b))