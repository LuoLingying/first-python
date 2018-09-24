import random
secert = random.randint(1, 10)
print('------------------我爱鱼C工作室--------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:")
while not temp.isdigit():
    print('please input a int num!')
    temp = input("reinput:")
else:
    guess = int(temp)
    n = 3
    while guess != secert and n > 0:
        n = n-1
        if guess > secert:
            print("哥，大了大了")
        else:
            print("嘿，小了小了")
        if(n > 0):
            temp = input("猜错了，请重新尝试:")
            while not temp.isdigit():
                print('please input a int num!')
                temp = input("reinput:")
            guess = int(temp)
        else:
            print("机会用光咯T_T")
    if guess == secert:
        print("我去，你是小甲鱼心里的蛔虫么？！")
        print("哼 猜中了也不会有奖励！")
    print("游戏结束，不玩啦 ^-^ ")

##备注
#while
#当while条件成立时一直执行while循环体，且可以在循环体内给guess赋值
#random
#循环模块，randint可以产生一个int型整数