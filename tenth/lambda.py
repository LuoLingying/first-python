# zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# 我希望打包的形式是灵活多变的列表而不是元祖
#（希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]这种形式），你能做到吗？
#（采用map和lambda表达式）

def three(x):
    if not x % 3:
        return x

print([three(x) for x in range(100)])

# 答案 可以以在后面添加if的方式实现
[ i for i in range(1, 100) if not(i%3)]


def square(x):
    return x**2
result = list(map(square,[1,2,3,4,5]))
print(result)


def xx(x,y):
    return [x, y]

print(list(map(lambda x,y:[x,y], [1,3,5,7,9], [2, 4, 6, 8, 10])))
