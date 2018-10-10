print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(0, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)


'''
一层一层循环筛选三种球的个数
当三个数和为8，则形成一个组合
'''