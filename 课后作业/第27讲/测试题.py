0 将一些对象表示在一起
# 确保里边包含的元素的唯一性
1 用frozenset()创建
2 len(setname)
3 报错
4 不一样 set1 = {[1, 2]} 集合内只能放一个可哈希的值,不能放一个list列表对象
set1 = set([1, 2])集合内有两个元素1,2 这两个元素
5 set1中只有一个值
6 set1.add(obj)  set1.remove(obj)或set1.discard(obj)或set1.pop()删除一个随机的数