def mybin(x):
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    else:
        return str(mybin(x//2)) + str(x%2)

num = int(input('请输入一个数据:'))
print(mybin(num))

