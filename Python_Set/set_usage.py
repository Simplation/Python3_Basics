#!/usr/bin/env python
# -*- coding: utf-8 -*-

# set 集合的相关操作
# set 的作用: 去重; 关系测试

list_one = [1, 4, 5, 6, 3, 2, 6, 7, 5, 0]

list_one = set(list_one)

list_two = set([2, 4, 8, 9, 16, 32])

print(list_one, list_two)

# 关系测试
# 交集 intersection
# 符号：&
print(list_one.intersection(list_two))

# 并集 union
# 符号：|
print(list_one.union(list_two))

# 差集(1存在的2不存在的集合) difference
# 符号： -
print(list_one.difference(list_two))

# 父集 issuperset
print(list_one.issuperset(list_two))

# 子集 issubset
print(list_one.issubset(list_two))

# 对称差集 （取出1和2中都不存在的）
# 符号： ^
print(list_one.symmetric_difference(list_two))

# 判断两个集合是否存在交集
print(list_one.isdisjoint(list_two))  # Return True if two sets have a null intersection.

# 添加
list_one.add(14)  # 添加一项
print(list_one)

list_one.update([22, 33, 44])  # 添加多项
print(list_one)

# 移除
list_one.remove(1)
print(list_one)

# 长度
print(len(list_one))

# 判断是否在该集合中
# print(1 in list_one)
# print(1 not in list_one)

# 删除
list_one.pop()  # 随机删除
print(list_one)

# discard 和 remove 的差不多相同， remove 移除不存在的元素会报错，但是 discard 不会
list_one.discard(666)
