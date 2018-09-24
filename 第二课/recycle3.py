temp = input("please input a num:")
while(not temp.isdigit()):
    print('please input a int num!')
    temp = input("reinput:")
else:
    temp = int(temp)
    while temp:
        i = temp -1
        while i:
            print(' ', end = '')
            i = i - 1
        j = temp
        while j:
            print('*', end = '')
            j = j - 1
        print()
        temp = temp - 1