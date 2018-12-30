#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import time

from timeCount.timeDecorator import clock       # 导入装饰器函数
"""
字符串拼接中：''.join() 和 + 的效率比较，数据量大时join明显占优
总结：
连接字符串时，应优先选择使用 join 而不是 +
"""

# 生成测试所需要的字符串列表, 10000为字符串连接的数目
str_list = ["it is a long value string will not keep in memory" for n in range(1000)]


def join_test():
    """ join对应的测试数据 """
    return ''.join(str_list)


def plus_test():
    """ 直接使用 + 连接符 """
    result = ''
    for i, v in enumerate(str_list):
        result += v
    return result


@clock
def time_test():
    """ 时间测试函数，睡眠1s """
    time.sleep(1)


if __name__ == "__main__":
    join_timer = timeit.Timer("join_test()", "from __main__ import join_test")
    print(join_timer.timeit(number=10000))

    plus_timer = timeit.Timer("plus_test()", "from __main__ import plus_test")
    print(plus_timer.timeit(number=10000))

    """ 这里还使用了计时装饰器，所以显示两个时间 """
    time_timer = timeit.Timer("time_test()", "from __main__ import time_test")
    print(time_timer.timeit(number=1))

