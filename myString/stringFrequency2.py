#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
编写一个Python程序来计算字符串中的字符个数（字符频率）
方法二： 简单判断, 原理还是调用了Python内置函数str.count(i)
"""

currentStr = input("input a sentence: ").replace(' ', '')  # 输入字符串并去掉空格
newStr = ''

for i in currentStr:
    if currentStr.count(i) <= 1:   # 如果字符数为1
        newStr += i
        newStr += ':'
        newStr = newStr + str(1) + ' '
    else:                          # 字符数大于1的情况
        if newStr.count(i) < 1:
            newStr += i
            newStr += ':'
            newStr = newStr + str(currentStr.count(i)) + ' '

print(currentStr, newStr)


