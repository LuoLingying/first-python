temp = input("please input a num:")
while(not temp.isdigit()):
    print('please input a int num!')
    temp = input("reinput:")
else:
    temp = int(temp)
    i = 0
    while i <= temp:
        for i in range(temp):
            print(' ' * temp + '*' * temp)
            temp = temp-1

'''
while后面可以不用括号
直接while not temp.isdigit():