name = input('请输入要读取的文件名:')
old = input('请输入要替换的字符:')
new = input('请输入替换后的字符:')

content = []
i = 0
fr = open(name)
for eachline in fr:
    if old in eachline:
        eachline = eachline.replace(old, new)
        i += 1
    content.append(eachline)
fr.close()

print('文件', name, '中共有', i, '个【', old, '】')
print('你确定要把所有的【', old, '】换成【', new, '】么？')
answer = input('【yes/no】')

if answer == 'yes':
    fw = open(name, 'w')
    fw.writelines(content)
    fw.close()