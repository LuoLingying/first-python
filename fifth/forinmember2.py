member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for elem in member:
    if(isinstance(elem, int)):
        print(elem)
    else:
        print(elem, end='')