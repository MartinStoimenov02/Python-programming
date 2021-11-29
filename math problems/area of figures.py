def square(a):
    return a**2

def rect(a,b):
    return a*b

def triangle(a,b):
    return (a*b)/2

fig=input("fig(square/rectangle/triangle):")

if fig=='square':
    x=int(input("side:"))
    print(square(x))

if fig=='rectangle':
    x=int(input("side a:"))
    y=int(input("side b:"))
    print(rect(x,y))

if fig=='triangle':
    x=int(input("side a:"))
    y=int(input("side b:"))
    print(triangle(x,y))
