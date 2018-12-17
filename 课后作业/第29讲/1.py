name = input('请输入文件名:')
contents = []
contents.append(input('请输入内容【单独输入":w"保存退出】'))
flag = 1
while flag == 1:
    line = input()
    if line == ':w':
        flag = 0
    else:
        contents.append(line)
f = open(name, 'x')
f.writelines(contents)
f.close()


'''
1. while 可以不用要一个flag来改变条件的值，在循环体内需要跳出循环时，可以直接使用break

2. 需要每次写的内容都换行用   '%s\n' % string  格式化后 需要每次只写入一句话
writelines针对序列时 会把序列里的每一个元素遍历写入 但是不会给每句换行
f.writelines('%s\n' % contents) 而这种写法 会把contents当成一个字符串 将序列整体写入文件中
---['从明天起 做一的人', '劈柴 喂马 周游世界', '我有一所房子', '面朝大海', '春暖花开']
并不会分行

3. 为了达到一个输出换行的处理 可以提示语句用print的方式 而真正的输入用单独的input()处理
可以保证输入统一
'''
