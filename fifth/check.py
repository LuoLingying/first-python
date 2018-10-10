# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

secert = input('请输入需要检查的密码组合:').lower()
n,a,b,c = 0,0,0,0
str1 = '你的密码安全级别评级为:level\n\
请安以下方式提升您的安全级别\
\n\t1. 密码必须由数字、字母及特殊字符三种组合\
\n\t2. 密码只能由字母开头\
\n\t3. 密码长度不能低于16位'

for i in secert:
    if(i in '~!@#$%^&*()_=-/,.?<>;:[]\{\}|/\\'):
        a += 1
    if(i in '0123456789'):
        b += 1
    if(i in 'abcdefghijklmnopqrstuvwxyz'):
        c += 1
if a > 0:
    n += 1
if b > 0:
    n += 1
if c > 0:
    n += 1
if a+b+c < len(secert):
    print('密码必须由数字、字母及特殊字符组成')
elif(secert.isalnum()):
    print(str1.replace('level','低'))
elif(n == 2):
    print(str1.replace('level','中'))
elif(n == 3 and secert[0].isalpha()):
    print('你的密码安全级别评级为:高\n请继续保持')
print('n=', n)
print('\na=', a)
print('\nb=', b)
print('\nc=', c)
