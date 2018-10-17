def esum(*params):
    'a) 计算打印所有参数的和乘以基数（base=3）的结果'
    'b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。'
    thesum = 0
    base = 3
    if params[len(params)-1] == 5:
        base = 5
        thesum -= params[len(params)-1] * 5
    for num in params:
        thesum += num * base

    return thesum

print(esum(1,2,3))