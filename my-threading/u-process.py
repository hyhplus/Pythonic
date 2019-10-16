#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
并发数字运算
I/O密集型的任务适合于多线程，而CPU密集型的任务则适合用多进程。
在下面的例子里，我们将找出100万个20000到100000000之间随机数的质数。

多进程运算： 本机测试结果 使用多进程 跟 不使用多进程 比较，多进程并没有速度上的优势，甚至更慢
"""
import time
import random
from multiprocessing import Pool


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


def execute_process(i):
    rand = random.randint(20000, 100000000)
    print(calculate_prime_factors(rand))


def main():
    pool = Pool(processes=4)
    pool.map_async(execute_process, range(100000))
    pool.close()
    pool.join()


if __name__ == '__main__':
    print("开始运算")
    t0 = time.time()
    main()
    t1 = time.time()
    total_time = t1 - t0
    print("执行时间：", total_time)

