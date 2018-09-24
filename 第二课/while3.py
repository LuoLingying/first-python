#解决
temp = input("please input a num:")
while(not temp.isdigit()):
    print('please input a int num!')
    temp = input("reinput:")
else:
    temp = int(temp)
    i = 1
    while i <= temp:
        print(temp)
        temp = temp-1


'''
实现了功能 但是isalpha()判断不好 '1a'也可以正确输入就报错了
应该用isdigit的取反 取反的符号
not

else
循环语句可以有 else 子句
它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行
但循环被break终止时不执行
例test1
'''