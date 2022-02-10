import time
h=int(input("hour: "))
m=int(input("minutes: "))
while True:
    for i in range(h,24):
        for j in range(m,60):
            h=0
            m=0
            print(f"{i}:{j}")
            for k in range(1,60):
                time.sleep(1)
            j+=1
        i+=1