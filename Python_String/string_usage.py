#!/usr/bin/env python
# encoding: utf-8
"""
@file: string_usage.py
@time: 2018-08-22 17:39
@desc: string 的相关用法
"""

if __name__ == "__main__":
    # 1、拼接字符串
    # 1.1、使用 + 来拼接，只能操作相同类型
    a = "正在学习"
    b = "Python"
    c = a + b
    print(c)    # 正在学习Python

    # 1.2、使用占位符来拼接字符串
    a = 'Py'
    b = 'thon'
    print('%s%s' % (a, b))    # Python

    # 2、字符串复制
    # 2.1、使用等号进行字符串的复制
    a = 'copy string...'
    print(a)        # result:copystring...

    b = a
    print(b)        # result:copy string...

    # 3、字符串长度
    # 使用len()函数获取字符串的长度

    A = 'copy string...'
    print(A)        # result:copy string...

    print(len(A))   # result:14

    # 4、字符串大小写转换(如果不进行重新赋值操作，原数据是不会发生变化的)
    # 4.1、将小写转换成大写
    a = 'copy, python'
    a.upper()  # 将小写完全变成大写
    print(a)   # result:'COPY, PYTHON'

    print(a)   # result:'copy, python'  # 原数据没有改变

    b = a.upper()  # 进行重新赋值，就会发生变化
    print(b)   # result:'COPY, PYTHON'

    # 4.2、将大写转换成小写
    c = b.lower()
    print(c)   # result:'copy, python'

    # 4.3、只改变首字符的大小写
    print(a)   # result:'copy, python'

    a.capitalize()  # 改变首字母为大写
    print(a)   # result:'Copy, python'

    print(a)   # result:'copy, python'

    b = a.capitalize()
    print(a)   # result:'Copy, python'

    print(b)   # result:'copy, python'

    # 4.4、判断首字母是否是大写(不含有逗号，且首字母大写的情况才是正确)
    a = 'Hello, python'  # 含有逗号的情况,直接返回 False。第一个是大写，第二个是小写
    print(a.istitle())   # result:False

    a = 'Hello, Python'
    print(a.istitle())   # result:True

    a = 'HelloPython'
    print(a.istitle())   # result:True

    # 4.5、判断字符串是否都是大写
    a = 'HelloPython'
    print(a.isupper())   # result:False

    print(a.upper().isupper())  # result:True

    a = 'Hello,Python'
    print(a.islower())   # result:False

    print(a.lower().islower())   # result:True

    # 5、给字符串编号(从左到右是是从0开始)
    a = 'Hello, World!'
    print(len(a)) # result:13

    print(a[0])   # result:'H'

    print(a[9])   # result:'r'

    print(a[-1])  # 从右到左是从-1开始的
    # result:'!'

    # 6、字符串截取 ：
    a = 'Hello,World'
    print(a[2:5])  # 从a开始到b结束
    # result:'llo'

    print(a[3:])  # 从a开始，截取到结束
    # 'lo,World'

    print(a[:5])  # 从开始位置截取到b位置
    # result:'Hello,'

    # 7、去掉字符串的空格
    a = ' Hello '
    print(a.strip())  # 去掉前后的空格
    # result:'Hello'

    print(a)      # result:' Hello '

    print(b.lstrip())  # 去掉前面的空格
    # result:'Hello '

    print(b.rstrip())  # 去掉后面的空格
    # result:' Hello'

