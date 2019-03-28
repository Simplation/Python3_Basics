#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建一个字典
# key-value
info = {
    'stu01': 'a',
    'stu02': 'b',
    'stu03': 'c'
}

# 查找：根据 key 取出 value
print(info['stu01'])
print(info.get('stu04'))  # 有查找的 key 就返回，没有的话就返回 None
print('stu04' in info)  # 判断 key 是否在该字典中，存在的话返回 True，否则返回 False
# info.has_key('stu04')    # 和上边的效果一样，但是该语法存在于 py2.x 中



# 修改：根据 key 来修改 value (如果存在的话就修改，不存在的话就创建)
info['stu02'] = 'B'
info['stu04'] = 'd'

# 删除
# del info['stu04'] # del 是 python 内置的一个函数
# info.pop('stu04') # 必须指定删除的 key
info.popitem()  # 随机删除字典中的一项

print(info)

# 字段的嵌套操作
# 这种示例仅供参考， key 值一般不建议、设置成中文
av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

# 更新大陆中的二个 value
av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"

# 创建默认值；（字典中存在 key 的话不会创建，不存在的话则创建，值是 key 所对应的 value）
av_catalog.setdefault("大陆", {"www.baidu.com": [1, 2]})
print(av_catalog)

# 取出所有的 key
print(av_catalog.keys())

# 取出所有的 value
print(av_catalog.values())

# 两个字典进行合并操作，交叉的部分进行更新覆盖，其他的进行创建
# info.update(av_catalog)

# 将字典转换成列表
print(info.items())

# 初始化一个新的字典，并赋值给 key 一个默认的值
c = dict.fromkeys([1, 2, 3], 'test')
print(c)

'''
小示例：演示一个坑！！！
'''
sample = dict.fromkeys([1, 2, 3], [1, {'name': 'Simpaltion.WANG'}, 6])
print(sample)

# 更改字典中的 name 值
sample[2][1]['name'] = 'Jack'  # 共同指向同一块内存地址，做修改操作的时候会都进行修改
print(sample)

# 循环字典操作
info = {
    'stu01': 'a',
    'stu02': 'b',
    'stu03': 'c',
    'stu04': 'd',
    'stu05': 'e'
}

# 循环字典的两种方式，方式1 的效率更高

# 方式1：通过 key 来取出对应的 value
for i in info:
    print(i, info[i])

# 方式2： 先将字典转换成列表，然后再取值
for k, v in info.items():
    print(k, v)
