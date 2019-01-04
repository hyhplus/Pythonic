#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写一个Python程序来计算字符串中的字符个数（字符频率）
方法一： 使用内置函数
"""

myString1 = "just a test string for this stringFrequency module."
myString = input("input strings：")    # input strings：freeze
myString = myString.replace(' ', '')   # 去掉空格
newDict = {}

for i in myString:
    newDict[i] = myString.count(i)

print(newDict)                         # {'f': 1, 'r': 1, 'e': 3, 'z': 1}





