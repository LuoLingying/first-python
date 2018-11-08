res = []
def digit(x):
    if x > 0:
        res.insert(0,x%10)
        digit(x//10)
    return res

print(digit(12345))