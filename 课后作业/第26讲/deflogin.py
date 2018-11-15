def login():
    users = {}
    while 1:
        print('|--- 新建用户: N/n ---|')
        print('|--- 登录账号: E/e ---|')
        print('|--- 退出程序: Q/q ---|')
        order = input('|--- 请输入指令码:').upper()
        if order == 'N':
            name = input('请输入用户名:')
            while name in users:
                name = input('此用户名已经被使用,请重新输入:')
            else:
                passwd = input('请输入密码:')
                users[name] = passwd
                print('注册成功,赶紧试试登录吧^-^')

        if order == 'E':
            name = input('请输入用户名:')
            while name not in users:
                name = input('您输入的用户名不存在,请重新输入:')
            else:
                passwd = input('请输入密码:')
                while users[name] != passwd:
                    passwd = input('密码有误,请重新输入:')
                else:
                    print('欢迎进入XX系统...')
    
        if order == 'Q':
            break
        
        if order != 'N' and order != 'E' and order != 'Q':
            print('您的输入有误')            

    print('|--- 感谢使用XX系统 ---|')

login()