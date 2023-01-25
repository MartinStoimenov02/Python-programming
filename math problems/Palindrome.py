def pal(a):
    lst=[]
    while a>0:
        lst.append(a%10)
        a=a//10

    if lst==lst[::-1]:
        return "the number is palindrome"

    else:
        return "the number isn't palindrome"

b=int(input("number:"))
print(pal(b))
