temp = int(input("please input a num:"))
if(~isinstance(temp, int)):
    print('please input a int num!')
    temp = input("reinput:")
else:
    num = int(temp)
    i = 1
    while i <= num:
        print(i)
        i = i+1
    