temp = int(input("please input a num:"))
if(isinstance(temp, int)):
    i = 1
    while i <= temp:
        print(temp)
        temp = temp-1
else:
    print('please input a int num!')
    temp = input("reinput:")

'''
遗留问题
如果没有输一个整数，int()强转时就报错了
怎么样在强转之前避免报错而告诉用户输入一个整数
输进来都是一个字符串，用int转 是数字字符串成功，不是数字字符串报错
但是直接用isinstance呢又都是字符串
*怎么判断是一个数字型字符串还不报错
'''
    
    