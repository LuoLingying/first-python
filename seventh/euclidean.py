def gcd(x, y):
    if not y:
        return x
    else:
        return gcd(y, x%y)

print(gcd(8, 12))

# 辗转相除法
# 如果x小于y, x%y = x, 所以会变成gcd(y,x) 大的数会始终跑到前面
'''
gcd(12,8)
gcd(8,4)
gcd(4,0)
4

gcd(15,2)
gcd(2,1)
gcd(1,0)
1

gcd(15,3)
gcd(3,0)
3

gcd(100,30)
gcd(30,10)
gcd(10,0)
10

gcd(20,7)
gcd(7,6)
gcd(6,1)
gcd(1,0)
1
'''