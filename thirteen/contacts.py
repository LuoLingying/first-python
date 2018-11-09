print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有联系人 ---|')
print('|--- 4:退出通讯录程序 ---|')

contacts = {}
order = 0
while order-4 != 0:
    order = int(input('请输入相关的指令代码:'))
    if order == 1:
        name = input('请输入联系人姓名:')
        if name in contacts.keys():
            print(name, ':', contacts[name], '\n')
        else:
            print('联系人不存在\n')
    elif order == 2:
        name = input('请输入联系人姓名:')
        if name in contacts.keys():
            print('你输入的姓名在通讯录中已存在 ->>', name, ':', contacts[name])
            answer = input('是否修改用户资料(Y/N)')
            if answer.upper() == 'Y':
                phone = input('请输入用户联系电话:')
                contacts[name] = phone
            elif answer.upper() != 'N':
                print('你的输入有误\n')
        else:
            phone = input('请输入用户联系电话:')
            contacts[name] = phone
            print('\n')
        print('\n')        
    elif order == 3:
        name = input('请输入联系人姓名:')
        if name in contacts.keys():
            contacts.pop(name)
            print('\n')            
        else:
            print('联系人不存在\n')
    elif order == 4:
        print('',end='')
    else:
        print('你的输入有误\n')
print('|--- 感谢使用通讯录程序 ---|')