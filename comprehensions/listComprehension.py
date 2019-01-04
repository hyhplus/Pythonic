#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from timeCount.timeDecorator import clock
"""
比较for循环和列表推导式的运行速度
"""


@clock
def for_even(number):
    evens = []
    for i in range(number):
        if i % 2 == 0:
            evens.append(i)
    return evens


@clock
def list_comprehension(number):
    return [i for i in range(number) if i % 2 is 0]


for_even(10)
list_comprehension(10)

# [0.00000939s] for_even(10) -> [0, 2, 4, 6, 8]
# [0.00000227s] list_comprehension(10) -> [0, 2, 4, 6, 8]
