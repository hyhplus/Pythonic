#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字典推导式：字母大小写合并; 快速更换key和value;
"""

case = {'a': 10, 'b': 34, 'A': 7, 'z': 3}

case_frequency = {
    k.lower(): case.get(k.lower(), 0) + case.get(k.upper(), 0)
    for k in case.keys()
}

print(case_frequency)   # Output: {'a': 17, 'b': 34, 'z': 3}


""" 快速更换key和value """
case = {'a': 10, 'b': 34}
case_frequency = {v: k for k, v in case.items()}
print(case_frequency)   # Output: {10: 'a', 34: 'b'}

case_frequency = {k: v-9 for k, v in case.items()}
print(case_frequency)   # Output: {'a': 1, 'b': 25}

