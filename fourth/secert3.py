tsecert = 'FishC.com'
n = 3
while n:
    secert = input('请输入密码:')
    if '*' in secert:
        print('密码中不能有*,你还有', n, '次机会', end = '')
    elif(secert != tsecert):
        n -= 1
        print('密码输入错误,你还有', n, '次机会', end = '')
    else:
        print('密码正确,进入程序...')
        break