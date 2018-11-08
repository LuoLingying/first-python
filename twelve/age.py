# 有5个人坐在一起，问第五个人多少岁？
# 他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。
# 问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

def get_age(age, n):
    if n > 1:
        return get_age(age+2, n-1)
    else:
        return age

age = int(input('请输入第一个人年龄:'))
num = int(input('请输入共有几个人:'))
print('第', num, '个人的年龄是', get_age(age, num), '岁.')