#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 《深入理解Python特性》学习笔记之搞笑的函数
# 1 函数是 Python 的对象
"""
1. Python 中一切皆为对象，函数也不例外。可以将函数分配给变量或存储在数据结构中。
2. 作为头等对象，函数还可以被传递给其他函数或作为其他函数的返回值。
3. 头等函数的特性可以用来抽象并传递程序中的行为。
4. 函数可以嵌套，并且可以捕获并携带父函数的一些状态。具有这种行为的函数称为闭包。
5. 对象可以被设置为可调用的，因此很多情况下可以将其作为函数对待。
"""


# 1.1 函数是对象
def yell(text):
    return text.upper() + '...'


bark = yell
print(bark)             # <function yell at 0x0000027E7DDAD1E0>
print(yell)             # <function yell at 0x0000027E7DDAD1E0>
demo1_1 = bark("Hello world | function test demo 1")
print(demo1_1)          # HELLO WORLD | FUNCTION TEST DEMO 1...

del yell
# yell("Hello")         # NameError: name 'yell' is not defined

hi = bark("Hello")
print(hi)               # HELLO...
print(bark.__name__)    # yell


# 1.2 函数可传递给其他函数
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


print(greet(bark))      # HI, I AM A PYTHON PROGRAM...


"""
Python 中具有代表性的高阶函数是内置的 map 函数。map 接受一个函数对象和一个可迭代
对象，然后在可迭代对象中的每个元素上调用该函数来生成结果。
下面通过将 bark 函数映射到多个问候语中来格式化字符串：
"""
print(list(map(bark, ['hello', 'hey', 'hi'])))   # ['HELLO...', 'HEY...', 'HI...']


# 1.3 嵌套函数
def speak(text):
    def whisper(t):
        return t.upper() + '!!!'
    return whisper(text)


print(speak('Hello, World'))        # HELLO, WORLD!!!


# 1.4 闭包示例
def get_speak_func(text, volume):
    # 内部函数 whisper 和 _yell，注意其中并没有 text 参数
    def whisper():
        return text.lower() + '...'

    def _yell():
        return text.upper() + '!'
    if volume > 0.5:
        return _yell
    else:
        return whisper


hello = get_speak_func('Hello, World', 0.7)()
print(hello)        # Output: 'HELLO, WORLD!'


# 2 lambda 是单表达式函数
"""
简单示例
```
>>> add = lambda x, y: x + y
>>> add(5, 3)
8
```
"""

# 函数表达式
expert = (lambda x, y: x + y)(5, 3)
print(expert)       # 8

# lambda 使用场景：排序
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
tuples = sorted(tuples, key=lambda x: x[1], reverse=False)
print(tuples)   # [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

# 将lambda 和map()或filter()结合起来构建复杂的表达式也很难让人理解，此时用列表
# 解析式或生成器表达式通常会清晰不少：
"""
# 有害：
>>> list(filter(lambda x: x % 2 == 0, range(16)))
[0, 2, 4, 6, 8, 10, 12, 14]

# 清晰：
>>> [x for x in range(16) if x % 2 == 0]
[0, 2, 4, 6, 8, 10, 12, 14]
"""

# 3 装饰器的力量
"""
装饰器的一大用途是将通用的功能应用到现有的类或函数的行为上，这些功能包括：
1 日志（logging）
2 访问控制和授权
3 衡量函数，如执行时间
4 限制请求速率（rate-limiting ）
5 缓存，等等
"""


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


text = say('Jane', 'Hello, World')
print(text)
# TRACE: calling say() with ('Jane', 'Hello, World'), {}
# TRACE: say() returned 'Jane: Hello, World'
# Jane: Hello, World


# Python 装饰器写日志
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if func.__name__ == "debug":
            msg = "debug {}".format(args[0])
        elif func.__name__ == "info":
            msg = "info {}".format(args[0])
        else:
            msg = "unknown {}".format(args[0])
        return func(msg, **kw)
    return wrapper


@log
def debug(msg):
    print(msg)


@log
def info(msg):
    print(msg)


if __name__ == "__main__":
    debug("bug!")
    info("msg.")


# 4 有趣的 *args 和 **kwargs
# *args 和**kwargs 用于在Python 中编写变长参数的函数。
# *args 收集额外的位置参数组成元组。**kwargs 收集额外的关键字参数组成字典。
def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# print(foo())          # TypeError: foo() missing 1 required positional argument: 'required'

foo('hello')            # hello

foo('hello', 1, 2, 3)
# hello
# (1, 2, 3)

foo('hello', 1, 2, 3, key1='value', key2=999)
# hello
# (1, 2, 3)
# {'key1': 'value', 'key2': 999}


# 5 函数参数解包
# * 和 ** 操作符有一个非常棒但有点神秘的功能，那就是用来从序列和字典中“解包”函数参数。
# 高效使用参数解包有助于为模块和函数编写更灵活的接口。

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


express = (x * x for x in range(3))
print_vector(*express)      # <0, 1, 4>

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)    # <1, 0, 1>
print_vector(*dict_vec)     # <y, z, x>

# 6 返回空值
# Python 在所有函数的末尾添加了隐式的 return None 语句。因此，如果函数没有指定返回
# 值，默认情况下会返回 None。

# 返回空值是 Python 的核心功能，但是使用显式的 return None 语句能更清楚地表达代码的意图。


def foo1(value):
    """建议显示说明返回值 None，方便以后维护"""
    if value:
        return value
    else:
        return None


def foo2(value):
    """纯return 语句，相当于`return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """无return 语句，也相当于`return None`"""
    if value:
        return value
