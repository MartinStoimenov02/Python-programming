def sum(a,b):
    return a+b

def razl(a,b):
    return a-b

def umn(a,b):
    return a*b

def de(a,b):
    return a/b

op=input("operation(+,-,*,/):")
if op=="+":
    x=int(input("a="))
    y=int(input("b="))
    print(sum(x,y))

if op=="-":
    x=int(input("a="))
    y=int(input("b="))
    print(razl(x,y))

if op=="*":
    x=int(input("a="))
    y=int(input("b="))
    print(umn(x,y))

if op=="/":
    x=int(input("a="))
    y=int(input("b="))
    if y==0:
        print("na 0 ne se deli!")
    else:
        print(de(x,y))
