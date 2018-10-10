member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for elem in member:
    if(member.index(elem) % 2 > 0):
        print(elem)
    else:
        print(elem, end='')