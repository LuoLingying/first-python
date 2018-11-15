import random
secert = random.randint(1,10)
guess = input('猜猜随机数产生的数是几:')
while not guess.isdigit():
    guess = input('请输入一个1-10的整数:')
else:
    guess = int(guess)
    n = 3
    while guess != secert and n > 0:
        n -= 1
        if guess > secert:
            print('大了')
            guess = input('请重新输入:')
            while not guess.isdigit():
                guess = input('请输入一个1-10的整数:')
            else:
                guess = int(guess)
        elif guess < secert:
            print('小了')
            guess = input('请重新输入:')
            while not guess.isdigit():
                guess = input('请输入一个1-10的整数:')
            else:
                guess = int(guess)
        else:
            print('猜对了')
            break
    print('游戏结束')
