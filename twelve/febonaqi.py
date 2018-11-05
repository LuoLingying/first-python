def febonaqi(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    return febonaqi(x-1) + febonaqi(x-2)

print(febonaqi(36)) 
