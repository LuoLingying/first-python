tsecert = 'FishC.com'
secert = input('请输入密码:')
n = 3
while n > 1:
    for i in secert:
        if(i == '*'):
            print('密码中不能有*,你还有', n, '次机会,请重新输入:')
            secert = input()
            break
    if(secert != tsecert):
        n -= 1
        print('密码输入错误,你还有', n, '次机会,请重新输入:')
        secert = input()
    else:
        print('密码正确,进入程序...')
        break
else:
    print('你的机会已用完')


'''
1->3的改进
secert = input('请输入密码:')需要放在while里面
不然已经没有抽奖机会时，还告诉用户输入，输完之后告诉用户机会用完
for i in secert:
    if(i == '*'):
可直接用 if '*' in secert: 不需要循环后再去判断
'''