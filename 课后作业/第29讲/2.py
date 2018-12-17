file1 = input('请输入要比较的一个文件名')
file2 = input('请输入要比较的另一个文件名')
f1 = open(file1)
f2 = open(file2)
file1s = []
file2s = []
for eachline in f1:
    file1s.append(eachline)
f1.close()
for eachline in f2:
    file2s.append(eachline)
f2.close()

for num in range(0,len(file1s)):
    if file1s[num] != file2s[num]:
        print('第', num+1, '行不一样')
        for i in range(0,len(file1s[num])):
            if file1s[num][i] != file2s[num][i]:
                print('从', i+1, '位置开始不一样')
                break


# 除了用for循环文件读取每行 还可以用readline一行一行的读取文件