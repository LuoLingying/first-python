def shuixianhua():
    '如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。'
    '例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数'
    arr = []
    for i in range(100, 1000):
        unit = (i // 1) % 10
        ten = (i // 10) % 10
        hundred = (i // 100) % 10
        if i == unit**3 + ten**3 + hundred**3:
            arr.append(i)
    
    return arr

print(shuixianhua())
