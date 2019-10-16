#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
并发数字运算
I/O密集型的任务适合于多线程，而CPU密集型的任务则适合用多进程。
在下面的例子里，我们将找出100万个20000到100000000之间随机数的质数。

顺序运算：
"""
import time
import random


def calculate_prime_factors(n):
    factors = []
    d = 2
    while d*d == n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += d
    if n == 1:
        factors.append(n)
    return factors


def main():
    for i in range(1000000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


if __name__ == '__main__':
    print("开始运算")
    t0 = time.time()
    main()
    t1 = time.time()
    total_time = t1 - t0
    print("执行时间：", total_time)

