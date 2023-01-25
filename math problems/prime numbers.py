def simple(num):
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                return str(num)+" is not a prime number"
    return str(num)+" is a prime number"

n = int(input("Enter a number: "))
print(simple(n))
for i in range(2, n):
    print(simple(i))