def sum(a,b):
    return a+b

def razl(a,b):
    return a-b

def umn(a,b):
    return a*b

def de(a,b):
    return a/b

while True:
    op=input("operation(+,-,*,/):")
    if op=="+" or op=="-" or op=="*" or op=="/":
        break
    else:
        print("please input a valid operator!") 

while True:
    try:
        x=float(input("a="))
        y=float(input("b="))
        break
    
    except ValueError:
        print("Please input a number!")
    
if op=="+":
    print(sum(x,y))

if op=="-":
    print(razl(x,y))

if op=="*":
    print(umn(x,y))

if op=="/":
    try:
        print(de(x,y))
    except ZeroDivisionError as error:
        print(error)