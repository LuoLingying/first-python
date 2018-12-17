name = input('请输入要读取的文件名:')
numstr = input('请输入要读取的行数【格式2:5 :4 2:】')

(start, end) = numstr.split(':', 1)
if start == '':
    start = 0
if end == '':
    end = 1000

i = 0
f = open(name)
for eachline in f:
    i += 1
    if i >= int(start) and i < int(end):
        print(eachline)
    if i == int(end):
        break
