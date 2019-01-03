#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写一个Python程序来计算字符串中的字符个数（字符频率）
"""

myString1 = "just a test string for this stringFrequency module."
myString = input("input strings：")
newDict = {}

for i in myString:
    newDict[i] = myString.count(i)

print(newDict)

# 示例结果：
# input strings：freeze
# {'f': 1, 'r': 1, 'e': 3, 'z': 1}

