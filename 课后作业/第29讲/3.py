name = input('请输入要读取的文件名:')
num = int(input('请输入要读取的行数:'))
i = 0
f = open(name)
for eachline in f:
    i+=1
    print(eachline)
    if i == num:
        break