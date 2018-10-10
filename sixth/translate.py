while True:
    num = input('请输入一个整数(输入Q结束程序):')
    if num == 'Q':
        break
    else:
        while not num.isdigit():
            print('please input a int num!')
            num = input("reinput:")
        else:
            num = int(num)
            print('十进制->十六进制:', num, '-> 0x', end = '')
            print('%x' % num)
            print('十进制->八进制:', num, '-> 0o', end = '')
            print('%o' % num)
            print('十进制->二进制:', num, '-> 0b', end = '')
            print(bin(num))

