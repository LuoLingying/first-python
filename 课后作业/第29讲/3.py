name = input('请输入要读取的文件名:')
num = int(input('请输入要读取的行数:'))
i = 0
f = open(name)
for eachline in f:
    i+=1
    print(eachline)
    if i == num:
        break

# 除了用for循环文件读取每行 还可以用readline一行一行的读取文件
# 且如果readline在循环里面，会每个循环读取一行 一行一行读下去
# 有一个指针，循环一次往下走一行
        