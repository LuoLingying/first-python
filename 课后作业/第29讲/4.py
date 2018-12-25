name = input('请输入要读取的文件名:')
numstr = input('请输入要读取的行数【格式2:5 :4 2:】')

print('文件%s' % name, end = '')
(start, end) = numstr.split(':', 1)
if start == '' and end == '':
    print('全文的内容如下：')
    start = 0
    end = 1000
elif start == '':
    print('从开始到%s行的内容是：' % end)
    start = 0
elif end == '':
    print('从%s行到末尾的内容是：' % start)
    end = 1000
else:
    print('从%s行到%s行的内容是：' % (start, end))
    
i = 0
f = open(name)
for eachline in f:
    i += 1
    if i >= int(start) and i < int(end):
        print(eachline)
    if i == int(end):
        break

# 字符串输出，如果有未知数的替换 一个的话在%后放一个值 两个及两个以上的话在后面跟一个序列
# f.read()读取剩余的所有字符，然后作为字符串返回 也就是读取剩余的所有 而不是一行一行的读取