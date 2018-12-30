#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import timeit
"""
装饰器实现程序函数的⏲计时器功能
"""


def clock(func):
    """ 计时装饰器 """
    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0   # 函数或程序运行的时间
        name = func.__name__                    # 函数名
        arg_str = ', '.join(repr(arg) for arg in args)   # 函数返回值
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def run(seconds):
    """ 测试计时的函数 """
    time.sleep(seconds)
    return time


@clock
def time_test():
    """ 测试计时的函数 """
    time.sleep(2)


if __name__ == '__main__':
    run(1.22)
    time_test()
