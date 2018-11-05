def hanoi(n, x, y, z):
    if n == 1:
        print(x, '=>', z)
    else:
        hanoi(n-1, x, z, y)
        print(x, '=>', z)
        hanoi(n-1, y, x, z)

num = int(input('please input the num of hanoi:'))
hanoi(num, 'x', 'y', 'z')