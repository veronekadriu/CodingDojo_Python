def a():
    return 5
print(a()) 

# Predict:5
# Output:5

def a():
    return 5
print(a()+a()) 

# Predict:10
# Output:10

def a():
    return 5
    return 10
print(a()) 

# Predict:5
# Output:5

def a():
    return 5
    print(10)
print(a())

# Predict:5
# Output:5

def a():
    print(5)
x = a()
print(x)

# Predict:5
# Output:

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) 

# Predict:- 3 5 8
# Output:- 3 5 error

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# Predict:25
# Output:25


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# Predict:100,10
# Output:100,10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# Predict:7 14 21
# Output:7 14 21

def a(b,c):
    return b+c
    return 10
print(a(3,5)) 

# Predict:8
# Output:8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# Predict:500 500 300 500
# Output:500 500 300 500


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  

# Predict:500 500 300 500 
# Output:500 500 300 500


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# Predict:500 500 300 300
# Output:500 500 300 300


def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# Predict:1 3 2
# Output:1 3 2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()


# Predict:1 3 5
# Output:1 3 5











