def febonaqi(x):
    x1 = 1
    x2 = 1
    x3 = 1
    while (x-2) > 0:
        x3 = x1+x2
        x1 = x2
        x2 = x3
        x -= 1
    return x3

print(febonaqi(36))
