import Calculator

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
    print(Calculator.sum(x,y))

if op=="-":
    print(Calculator.razl(x,y))

if op=="*":
    print(Calculator.umn(x,y))

if op=="/":
    try:
        print(Calculator.de(x,y))
    except ZeroDivisionError as error:
        print(error)
