for i in range(100, 1000):
    unit = (i // 1) % 10
    ten = (i // 10) % 10
    hundred = (i // 100) % 10
    if i == unit**3 + ten**3 + hundred**3:
        print(i)