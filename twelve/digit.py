# 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]

def get_digits(x):
    arr = []
    numstr = str(x)
    for i in numstr:
        arr.append(i)
    return arr

num = str(input('请输入一个数字:'))
print(get_digits(num))