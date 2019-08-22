def fibonacilist(num):
    fiblist = []
    a = 0
    b = 1
    if num == 0:
        print("invalid")
    elif num == 1:
        fiblist.append(a)
    elif num == 2:
        fiblist.append(a)
        fiblist.append(b)
    else:
        fiblist.append(a)
        fiblist.append(b)
        for x in range(2, num):
            c = a + b
            a = b
            b = c
            fiblist.append(c)
    for y in fiblist:
        print(y)

print("enter the range:")
a = int(input())
fibonacilist(a)


