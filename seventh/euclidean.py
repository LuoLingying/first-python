def gcd(x, y):
    if not y:
        return x
    else:
        return gcd(y, x%y)

print(gcd(7890, 123456))
