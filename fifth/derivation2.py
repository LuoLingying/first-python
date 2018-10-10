list1 = ['1.Just do it', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible isNothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼C工作室', '1.耐克']
list3 = [y[:] + ':' + x[2:] for x in list1 for y in list2 if x[0] == y[0]]
for each in list3:
    print(each)