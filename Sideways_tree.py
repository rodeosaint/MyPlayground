num_1 = int(input("Enter a number: "))
n = 0
while n <=num_1:
    t = 0
    while t <= n:
        print ("=", end="")
        r = 0
        while r <=num_1-3:
            print ("|", end="")
            r +=1
        t +=1
    print ("")
    n +=1

while n >=0:
    t = 0
    while t <= n:
        print ("=", end="")
        r = num_1-3
        while r >=0:
            print ("|", end="")
            r -=1
        t +=1
    print ("")
    n -=1